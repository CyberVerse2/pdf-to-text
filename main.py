from fastapi import FastAPI, File, UploadFile
import io
import PyPDF2

app = FastAPI()

@app.post("/convert-pdf-to-text")
async def convert_pdf_to_text(file: UploadFile = File(...)):
    # Read the PDF buffer from the uploaded file
    pdf_buffer = await file.read()

    # Create a BytesIO object from the PDF buffer
    pdf_bytes = io.BytesIO(pdf_buffer)

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_bytes)

    # Extract text from each page
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    return {"text": text}