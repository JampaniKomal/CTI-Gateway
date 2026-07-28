import os
from lxml import etree
from .feed_fetcher import FeedFetcher

class XMLProcessor:
    """
    Handles XML parsing via XPath, schema validation via XSD, and transformation via XSLT.
    """
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.xsd_path = os.path.join(base_dir, 'schemas', 'threat_model.xsd')
        self.xslt_path = os.path.join(base_dir, 'schemas', 'transform_to_siem.xslt')
        
        # Load XSD Schema
        with open(self.xsd_path, 'rb') as f:
            schema_root = etree.XML(f.read())
            self.schema = etree.XMLSchema(schema_root)
            
        # Load XSLT
        with open(self.xslt_path, 'rb') as f:
            xslt_root = etree.XML(f.read())
            self.transform = etree.XSLT(xslt_root)

    def process_feed_to_normalized_xml(self) -> bytes:
        """
        Fetches the feed, extracts IoCs using XPath, builds a normalized XML,
        validates it against the XSD, and returns the XML string.
        """
        fetcher = FeedFetcher()
        raw_xml = fetcher.fetch_raw_xml()
        
        # Parse the raw feed
        root = etree.fromstring(raw_xml)
        
        # Build normalized XML
        NSMAP = {None: "http://ctigateway.example.com/threat"}
        threat_report = etree.Element("{http://ctigateway.example.com/threat}ThreatReport", nsmap=NSMAP)
        indicators = etree.SubElement(threat_report, "{http://ctigateway.example.com/threat}Indicators")
        
        # XPATH EXTRACTION
        # Extracting items from the RSS feed
        items = root.xpath('//item')
        
        for item in items:
            indicator_elem = etree.SubElement(indicators, "{http://ctigateway.example.com/threat}Indicator")
            
            # Extract specific fields using relative XPath
            title = item.xpath('./title/text()')
            category = item.xpath('./category/text()')
            severity = item.xpath('./severity/text()')
            desc = item.xpath('./description/text()')
            pub_date = item.xpath('./pubDate/text()')
            source = item.xpath('./source/text()')
            
            # Populate our normalized structure
            if title:
                etree.SubElement(indicator_elem, "{http://ctigateway.example.com/threat}ID").text = title[0]
            if category:
                etree.SubElement(indicator_elem, "{http://ctigateway.example.com/threat}Type").text = category[0]
            if severity:
                etree.SubElement(indicator_elem, "{http://ctigateway.example.com/threat}Severity").text = severity[0]
            if desc:
                etree.SubElement(indicator_elem, "{http://ctigateway.example.com/threat}Description").text = desc[0]
            if pub_date:
                # Basic string map (In a strict production system, we'd parse and format as strict xs:dateTime)
                etree.SubElement(indicator_elem, "{http://ctigateway.example.com/threat}PublishedDate").text = pub_date[0]
            if source:
                etree.SubElement(indicator_elem, "{http://ctigateway.example.com/threat}Source").text = source[0]

        # XSD VALIDATION
        # Will raise an exception if the constructed XML is invalid
        try:
            self.schema.assertValid(threat_report)
        except etree.DocumentInvalid as e:
            raise Exception(f"XML Schema Validation Failed: {e}")

        return etree.tostring(threat_report, pretty_print=True, xml_declaration=True, encoding="UTF-8")

    def transform_to_html(self, normalized_xml: bytes) -> bytes:
        """
        Applies the XSLT to the normalized XML to generate a SIEM HTML dashboard.
        """
        dom = etree.fromstring(normalized_xml)
        newdom = self.transform(dom)
        return etree.tostring(newdom, pretty_print=True, encoding="UTF-8")
