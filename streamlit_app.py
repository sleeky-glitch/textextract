import streamlit as st
import fitz  # PyMuPDF
import easyocr
from PIL import Image
import io

# Set the title of the app
st.title("Gujarati Newspaper Text Extractor from PDF")

# Upload PDF file
uploaded_file = st.file_uploader("Choose a scanned PDF of a Gujarati newspaper", type=["pdf"])

if uploaded_file is not None:
    # Read the PDF file
    pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    # Initialize EasyOCR reader for Gujarati
    reader = easyocr.Reader(['gu'])  # 'gu' is the language code for Gujarati

    # Initialize a variable to hold the extracted text
    extracted_text = ""

    # Process each page in the PDF
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        pix = page.get_pixmap()  # Render page to an image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)  # Convert to PIL Image

        # Use EasyOCR to extract text from the image
        result = reader.readtext(img, detail=0, paragraph=True)  # Extract text as paragraphs
        page_text = "\n".join(result)  # Join paragraphs into a single string
        extracted_text += f"--- Page {page_num + 1} ---\n{page_text}\n\n"

    # Display the extracted text
    st.subheader("Extracted Text:")
    st.text_area("Text Output", extracted_text, height=300)
