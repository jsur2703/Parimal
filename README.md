# Parimal
This is a web-based prototype built using Streamlit and EasyOCR that allows users to upload an image containing both English and Hindi text. The application performs Optical Character Recognition (OCR) to extract the text from the image and provides a keyword search functionality within the extracted text.

# Features
-OCR for English and Hindi: Extracts text from an uploaded image in both English and Hindi using EasyOCR.<br />
-Image Upload: Users can upload images in PNG, JPG, or JPEG formats.<br />
-Keyword Search: Users can search for keywords within the extracted text, and matching results are highlighted.<br />
-Web Interface: The application uses Streamlit for an intuitive and simple web interface.<br />

# Prerequisites
Before running the application, ensure you have the following installed:
-Python 3.x<br />
-pip (Python package manager)<br />

# Installation
Clone the repository (if hosted on a platform like GitHub(bash):
git clone https://github.com/your-repo/ocr-hindi-english.git
cd ocr-hindi-english
Install the required Python libraries (bash):
pip install streamlit easyocr pillow numpy

# Running the Application
Open a terminal or command prompt in the project directory.<br />
Run the mentioned command to start the Streamlit app (bash): streamlit run app.py <br />
Once the app is running, a web page will automatically open in your browser at http://localhost:8501/. You can upload an image containing English and/or Hindi text and use the keyword search feature.

# How It Works
Upload an Image: Upload an image file (PNG, JPG, or JPEG) containing text in either English, Hindi, or both.<br />
Extract Text: The app uses EasyOCR to extract the text from the uploaded image, which is displayed in a text box.<br />
Keyword Search: Enter a keyword to search for within the extracted text. If the keyword is found, the matching sections will be displayed.<br />

# Dependencies
Streamlit: Used for building the web interface.<br />
EasyOCR: For performing Optical Character Recognition (OCR) on the uploaded images.<br />
Pillow: Used for handling image files.<br />
NumPy: For image array processing.<br />
