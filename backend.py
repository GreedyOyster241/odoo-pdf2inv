
import os
import xmlrpc.client
from flask import Flask, request
from dotenv import load_dotenv

# in order to run, use python odoo-pdf2inv/backend.py
# it will run on http://127.0.0.1:5000

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
if all([url, db, username, api_key]):
    try:
        uid = common.authenticate(db, username, api_key, {})
        models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
        print(f'Connected to Odoo with UID: {uid}')
        # Searches for products in the Odoo database
        products = models.execute_kw(
            db,
            uid,
            api_key,
            "product.product",
            "search_read",
            [[]],
            {
                "fields": ["id", "name", "default_code"],
                "limit": 5
            }
        )
        print(f'Available products: {products}')
        return products, 200
    except Exception as e:
        print('Connected to Odoo but failed to read models:', e)
        return 'Failed to connect to Odoo!', 500
else:
    print('Missing Odoo connection info in .env file')
    return 'Missing Odoo connection info!', 500


@app.route('/save', methods=['POST'])
# Writes text from contenteditable container to .env file
def save():
    data = request.get_json()
    text = data['text']

    with open('.env', 'a') as env_file:
        env_file.write(f'CONTENT="{text}"\n')

    return 'Content saved!', 200


if __name__ == '__main__':
    app.run(debug=True)
