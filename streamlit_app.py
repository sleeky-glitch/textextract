import streamlit as st
from google.cloud import vision
from google.cloud.vision import types
import io
from PIL import Image

# Set up Google Cloud Vision client
def create_vision_client():
    return vision.ImageAnnotatorClient()

# Function to perform OCR using Google Cloud Vision API
def detect_text(image):
    client = create_vision_client()
    content = image.read()
    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    if response.error.message:
        raise Exception(f'{response.error.message}')
    return texts[0].description if texts else ""

# Streamlit app
st.title("Gujarati OCR with Google Cloud Vision API")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the image file
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Perform OCR using Google Cloud Vision API
    try:
        extracted_text = detect_text(uploaded_file)
        st.subheader("Extracted Text:")
        st.write(extracted_text)
    except Exception as e:
        st.error(f"Error: {e}")
