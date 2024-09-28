# Parimal
import streamlit as st
from PIL import Image
import pytesseract
import re

# Function to extract text from image
def extract_text_from_image(image):
    return pytesseract.image_to_string(image)
# Function to search and highlight keywords in text
def highlight_keywords(text, keyword):
    highlighted_text = re.sub(f"({keyword})", r'<mark>\1</mark>', text, flags=re.IGNORECASE)
    return highlighted_text

# Streamlit app
def main():
    st.title("Image OCR and Keyword Search")
    uploaded_image = st.file_uploader("Upload an image for OCR", type=["png", "jpg", "jpeg"])
    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        extracted_text = extract_text_from_image(image)
        st.subheader("Extracted Text")
        st.text(extracted_text)
        keyword = st.text_input("Enter keyword to search")
        if keyword:
            st.subheader("Search Results")
            highlighted_text = highlight_keywords(extracted_text, keyword)
            st.markdown(f"<div style='white-space: pre-wrap;'>{highlighted_text}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
