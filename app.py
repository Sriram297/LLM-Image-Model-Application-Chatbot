from dotenv import load_dotenv 
import streamlit as st 
import os 
import google.generativeai as genai
from PIL import Image
import io

# Load environment variables
load_dotenv()  

# Configure Gemini API
genai.configure(api_key='GOOGLE_API_KEY')

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel('models/gemini-1.5-flash-latest')

def get_gemini_response(question, image):
    if question:
        response = model.generate_content([question, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title='Gemini Image Demo')
st.header('Gemini LLM Application')

# Input field
user_input = st.text_input('Input:', key='input')

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Submit button
submit = st.button('Submit')

# When submit is clicked
if submit:
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        response = get_gemini_response(user_input, image)
        
        st.subheader('The Response is:')
        st.write(response)
    else:
        st.warning("Please upload an image before submitting.")
