import streamlit as st
from PIL import Image
import pytesseract
import re

# Function to extract text from image
def extract_text_from_image(image):
    return pytesseract.image_to_string(image)

# Function to search and highlight keywords in text
def highlight_keywords(text, keyword):
    # Use regex to find the keyword and add highlighting
    highlighted_text = re.sub(f"({keyword})", r'<mark>\1</mark>', text, flags=re.IGNORECASE)
    return highlighted_text

# Streamlit app
def main():
    st.title("Image OCR and Keyword Search")

    # Step 1: Image Upload
    uploaded_image = st.file_uploader("Upload an image for OCR", type=["png", "jpg", "jpeg"])
    
    if uploaded_image:
        # Display the uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
        # Step 2: Extract Text from Image
        extracted_text = extract_text_from_image(image)
        st.subheader("Extracted Text")
        st.text(extracted_text)
        
        # Step 3: Keyword Search
        keyword = st.text_input("Enter keyword to search")
        
        if keyword:
            # Search for the keyword and highlight it
            st.subheader("Search Results")
            highlighted_text = highlight_keywords(extracted_text, keyword)
            
            # Display highlighted results with Streamlit's HTML component
            st.markdown(f"<div style='white-space: pre-wrap;'>{highlighted_text}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
