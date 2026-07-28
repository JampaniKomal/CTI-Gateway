import requests

# The endpoint where our Spyne SOAP service is running
url = "http://127.0.0.1:8000/"

# The SOAP Envelope (The XML request)
soap_body = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:soap="http://ctigateway.example.com/soap">
   <soapenv:Header/>
   <soapenv:Body>
      <soap:GetThreatDashboardHTML/>
   </soapenv:Body>
</soapenv:Envelope>
"""

# Headers to tell the server we are sending XML
headers = {
    'Content-Type': 'text/xml; charset=utf-8'
}

print("Sending SOAP Request to CTI Gateway...")
response = requests.post(url, data=soap_body, headers=headers)

print("\n--- SERVER RESPONSE ---\n")
print(response.text)

# You can save it to an HTML file to actually see the dashboard!
with open("dashboard_output.html", "w", encoding="utf-8") as f:
    # We strip out the SOAP envelope wrappers to just get the HTML content
    from xml.etree import ElementTree as ET
    root = ET.fromstring(response.content)
    # Extract the string inside the GetThreatDashboardHTMLResult tag
    result = root.find('.//{http://ctigateway.example.com/soap}GetThreatDashboardHTMLResult')
    if result is not None and result.text:
        f.write(result.text)
        print("\n[SUCCESS] The HTML dashboard has been saved to 'dashboard_output.html'. Open it in your browser!")
