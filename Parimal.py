import streamlit as st
from PIL import Image
from transformers import pipeline


# Load a model known to handle Hindi text well
'''ocr_model = pipeline("ocr", model="path_to_hindi_supported_model")
def extract_text(image):
    results = ocr_model(image)
    # Process results to extract text
    extracted_text = "\n".join([result['text'] for result in results])
    return extracted_text'''

# Load the OCR model
ocr_model = pipeline("ocr", model="path_to_GOT_model")

def extract_text(image):
    results = ocr_model(image)
    return results

# Streamlit UI
st.title("OCR and Document Search")
st.write("Upload an image to extract text and search for keywords.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])
keyword = st.text_input("Enter keyword to search:")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Perform OCR
    extracted_text = extract_text(image)
    st.subheader("Extracted Text:")
    st.write(extracted_text)

    # Search functionality
    if keyword:
        search_results = [line for line in extracted_text.split('\n') if keyword in line]
        st.subheader("Search Results:")
        for result in search_results:
            st.write(result)
