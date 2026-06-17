from flask import Flask  # type: ignore[import]
import os
import xmlrpc.client
from dotenv import load_dotenv  # type: ignore[import]

load_dotenv()

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

# Load Odoo connection info from .env file and connect before starting the server
url = os.getenv('ODOO_URL', 'http://localhost:8069')
db = os.getenv('ODOO_DB', 'odoo_db')
username = os.getenv('ODOO_USERNAME', 'admin')
api_key = os.getenv('ODOO_API_KEY', 'your_api_key')

common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
try:
    uid = common.authenticate(db, username, api_key, {})
    models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
    print(f'Connected to Odoo with UID: {uid}')
    try:
        # Use an empty domain to avoid version-specific fields like 'is_abstract'
        models_list = models.execute_kw(db, uid, api_key, 'ir.model', 'search_read', [[]], {'fields': ['name'], 'limit': 200})
        print(f'Available models (showing up to 200): {models_list}')
    except Exception as e:
        print('Connected to Odoo but failed to read models:', e)
except Exception as e:
    print('Failed to connect to Odoo:', e)


# TODO: Add API endpoints to interact with Odoo models as needed

# PDF upload & processing — simple step-by-step
#TODO: Add a POST endpoint (e.g. /upload) that accepts a file (multipart/form-data).
#TODO: Save the uploaded PDF to a temporary folder (./uploads or system temp).
#TODO: Extract text/data from the PDF using a library (recommended: pdfplumber or PyPDF2).
#TODO: Parse the extracted text to find fields you need (date, vendor, lines, total, etc.).
#TODO: Allow the user to instead ask the AI to parse the PDF by sending the extracted text to an AI model (e.g. OpenAI API) with a prompt to extract structured data.
#TODO: Map parsed fields to Odoo model data and call the XML-RPC API to create records.
#TODO: Handle errors gracefully (invalid PDF, parsing issues, Odoo API errors) and return informative messages to the frontend.
#TODO: Implement security measures (file type/size checks, authentication for API endpoints, etc.) to prevent abuse.
#TODO: Consider adding logging for debugging and monitoring purposes, especially for file uploads and Odoo interactions.
#TODO: Return a JSON response (success/failure) to the frontend and delete temp files.
# Notes: Add input validation, error handling, and security checks. For large or slow PDFs,
# consider processing in a background job (Celery, RQ) and returning a job ID.


if __name__ == '__main__':
    app.run(debug=True)
