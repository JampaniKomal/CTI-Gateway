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

You have two easy ways to test this SOAP web service:

### Option 1: Using the included Python Test Client (Easiest)
We have included a built-in SOAP client (`test_client.py`) so you don't need to install any external software.
1. Make sure your server is running (`python app.py`) in one terminal.
2. Open a second terminal, activate the virtual environment, and run:
   ```bash
   python test_client.py
   ```
3. The script will send a SOAP Request to the server, and the server will respond with the transformed HTML dashboard. 
4. The script automatically saves the result to `dashboard_output.html`. Double-click this file to view the SIEM dashboard in your browser!

### Option 2: Using SoapUI
If you want to test it like a true Enterprise developer using **SoapUI**:
1. Open **SoapUI**.
2. Click **New SOAP Project**.
3. In the "Initial WSDL" field, paste our server's WSDL URL: `http://127.0.0.1:8000/?wsdl`
4. Click OK. SoapUI will automatically read the WSDL and generate sample requests for `GetLatestThreatsXML` and `GetThreatDashboardHTML`.
5. Expand `GetThreatDashboardHTML`, open `Request 1`, and click the green **Play** button in the top left corner of the request window to send the SOAP envelope.
6. The raw XML or transformed HTML response will appear on the right side of your screen!
