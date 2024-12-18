import streamlit as st
from PIL import Image
import pytesseract

# Set the title of the app
st.title("Gujarati Newspaper Text Extractor")

# Upload image
uploaded_file = st.file_uploader("Choose a scanned image of a Gujarati newspaper", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the image file
    image = Image.open(uploaded_file)

    # Display the image
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Extract text from the image
    extracted_text = pytesseract.image_to_string(image, lang='gu')  # 'gu' is the language code for Gujarati

    # Display the extracted text
    st.subheader("Extracted Text:")
    st.write(extracted_text)
