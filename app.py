from werkzeug.serving import run_simple
from services.soap_service import wsgi_application

if __name__ == '__main__':
    print("=========================================================")
    print(" Starting CTI Gateway SOAP Service (XML & Web Services) ")
    print("=========================================================")
    print("WSDL is available at: http://127.0.0.1:8000/?wsdl")
    print("Press Ctrl+C to stop.")
    
    # Run the WSGI application on port 8000
    run_simple('127.0.0.1', 8000, wsgi_application, use_reloader=True)
