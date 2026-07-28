# Cyber Threat Intelligence (CTI) Gateway

**Course:** XML & Web Services (G7B38XWS)  
**Program:** B.Tech Computer Science & Engineering (Specialization in Cyber Security) - Semester VII

This project is a fully functional SOAP-based web service that aggregates real-time threat feeds, parses them using XML technologies, and serves them in a structured format ready for ingestion by SIEM platforms (like Splunk or Wazuh).

## Features & Course Requirements Met

1. **XML-based Request/Response:** Exposes a SOAP Web Service using Python's `spyne` framework.
2. **WSDL Contract:** Auto-generates a robust WSDL for client consumption.
3. **XPath Extraction:** Uses `lxml` and XPath to extract specific Indicators of Compromise (IoCs) like malicious IP addresses and CVE identifiers from raw XML feeds.
4. **Schema Validation (XSD):** Normalizes extracted data and validates it against a strict `threat_model.xsd` schema. Throws SOAP faults on validation failure.
5. **XSLT Transformation:** Uses `transform_to_siem.xslt` to transform the validated XML into an HTML SIEM dashboard.

## Technology Stack
- **Language:** Python 3.x
- **SOAP Framework:** `spyne` and `werkzeug`
- **XML Processing:** `lxml` (for XPath, XSD, and XSLT)

## How to Run

1. Create a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```
   *(Note: Ensure you have C++ Build Tools installed if installing `lxml` from source on newer Python versions).*

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the SOAP Gateway:
   ```bash
   python app.py
   ```

4. The WSDL will be accessible at: `http://127.0.0.1:8000/?wsdl`

## Client Testing
You can test the SOAP endpoint using **Postman** or **SoapUI** by creating a new SOAP request and pointing it to the WSDL URL. You can invoke methods like `GetLatestThreatsXML` and `GetThreatDashboardHTML`.
