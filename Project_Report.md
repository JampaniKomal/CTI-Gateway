# Practical Project Report: Cyber Threat Intelligence (CTI) Gateway

**Course:** XML & Web Services (G7B38XWS)
**Submitted By:** [Your Name / Student ID]
**GitHub Repository:** https://github.com/JampaniKomal/CTI-Gateway

---

## 1. Abstract
In modern cybersecurity, Security Information and Event Management (SIEM) systems require structured, validated threat data to monitor networks effectively. The Cyber Threat Intelligence (CTI) Gateway is a middleware application designed to ingest raw, unstructured XML threat feeds, extract critical Indicators of Compromise (IoCs), validate them against a strict schema, and serve them via a SOAP web service. The final output can be consumed by other systems or viewed as a beautifully formatted HTML dashboard generated entirely via XSLT transformations.

## 2. Objective
The primary objective of this project is to apply core XML and Web Service concepts to a real-world cybersecurity scenario. Specifically, the project demonstrates hands-on implementation of:
- **XML & XPath:** For data parsing and precise extraction of threat intelligence.
- **XML Schema (XSD):** For strict data validation, ensuring integrity before processing.
- **XSLT:** To transform validated XML data into a human-readable HTML user interface.
- **SOAP & WSDL:** To expose the application as a highly interoperable web service with a clear, auto-generated service contract.

## 3. Tools/Technologies Used
- **Programming Language:** Python 3.12
- **Web Service Framework:** `spyne` (for SOAP envelope handling and WSDL generation) and `werkzeug` (for WSGI server routing).
- **XML Processing Engine:** `lxml` (for high-performance XPath querying, XSD validation, and XSLT transformations).
- **Testing:** Custom Python `requests` client acting as a SOAP consumer.

## 4. System Design (Architecture)
The architecture follows a standard middleware integration pattern:
1. **Client Request:** A SOAP client sends a request to the CTI Gateway (`GetLatestThreatsXML` or `GetThreatDashboardHTML`).
2. **Data Ingestion & Extraction (XPath):** The gateway fetches raw XML threat data and uses XPath to filter out noise, extracting only CVEs, Malicious IPs, and File Hashes.
3. **Data Validation (XSD):** The extracted data is formed into a new XML tree and validated against `threat_model.xsd`. If validation fails, a SOAP fault is returned.
4. **Data Transformation (XSLT):** If requested, the validated XML is transformed using `transform_to_siem.xslt` into a stylized HTML dashboard.
5. **SOAP Response:** The gateway wraps the final XML or HTML payload in a SOAP envelope and returns it to the client.

## 5. Implementation / Code Snippets

### Core XML Schema (`threat_model.xsd`)
This schema ensures all threat data strictly adheres to our defined types (e.g., Severity must be LOW, MEDIUM, HIGH, or CRITICAL).
```xml
<xs:simpleType name="SeverityType">
    <xs:restriction base="xs:string">
        <xs:enumeration value="LOW"/>
        <xs:enumeration value="MEDIUM"/>
        <xs:enumeration value="HIGH"/>
        <xs:enumeration value="CRITICAL"/>
    </xs:restriction>
</xs:simpleType>
```

### XPath Extraction (`xml_processor.py`)
XPath is used to navigate the raw XML tree and extract precise IoC nodes.
```python
# Using XPath to extract threat items from the raw feed
items = root.xpath('.//item')
for item in items:
    title = item.xpath('./title/text()')[0]
    description = item.xpath('./description/text()')[0]
    # ... logic to categorize as IP, Hash, or CVE ...
```

### SOAP Service Definition (`soap_service.py`)
Using Spyne to define the SOAP endpoint that auto-generates the WSDL.
```python
class CTIGatewayService(ServiceBase):
    @rpc(_returns=Unicode)
    def GetThreatDashboardHTML(ctx):
        processor = XMLProcessor()
        normalized_xml = processor.process_feed_to_normalized_xml()
        html_dashboard = processor.transform_to_html(normalized_xml)
        return html_dashboard.decode('utf-8')
```

## 6. Screenshots

*(Instructions: Take screenshots on your computer and paste them below before saving to PDF/Word)*

**[PLACEHOLDER: Screenshot 1 - The WSDL in the browser]**
*(Take a screenshot of your browser showing the raw XML WSDL at `http://127.0.0.1:8000/?wsdl`)*

**[PLACEHOLDER: Screenshot 2 - The Python Test Client]**
*(Take a screenshot of your terminal after running `python test_client.py`, showing the "Sending SOAP Request..." text and the raw SOAP response)*

**[PLACEHOLDER: Screenshot 3 - The SIEM HTML Dashboard]**
*(Take a screenshot of the beautiful dark-mode dashboard opened in your web browser)*

## 7. Result / Conclusion
The project successfully meets all academic requirements by demonstrating a fully functional SOAP web service. The application successfully aggregates data, enforces strict schema validation using XSD, navigates complex node structures with XPath, and dynamically generates a user interface using XSLT. By applying these legacy enterprise protocols to modern threat intelligence, the project proves the continued relevance and power of XML technologies in securing enterprise architectures.

## 8. Future Scope
- **REST API Comparison:** Developing a parallel REST API using Flask or FastAPI to compare payload sizes and parsing speeds between SOAP/XML and REST/JSON.
- **Database Integration:** Storing validated IoCs in a relational database or a SIEM platform like Wazuh for historical tracking.
- **Authentication:** Implementing WS-Security to add encryption and digital signatures to the SOAP envelopes, ensuring only authorized clients can access the threat feeds.
