import streamlit as st
import fitz  # PyMuPDF
from omniparser import OmniParser
import io

# Set the title of the app
st.title("Gujarati Newspaper Text Extractor from PDF using OmniParser")

# Upload PDF file
uploaded_file = st.file_uploader("Choose a scanned PDF of a Gujarati newspaper", type=["pdf"])

if uploaded_file is not None:
    # Read the PDF file
    pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    # Initialize a variable to hold the extracted text
    extracted_text = ""

    # Process each page in the PDF
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        pix = page.get_pixmap()  # Render page to an image
        img_bytes = pix.tobytes()  # Get image bytes

        # Use OmniParser to extract text from the image
        parser = OmniParser()
        result = parser.parse_image(img_bytes)

        # Append the extracted text
        extracted_text += f"--- Page {page_num + 1} ---\n{result['text']}\n\n"

    # Display the extracted text
    st.subheader("Extracted Text:")
    st.text_area("Text Output", extracted_text, height=300)
