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
