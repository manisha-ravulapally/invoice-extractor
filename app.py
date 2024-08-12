import streamlit as st
import google.generativeai as genai
from PIL import Image
from pdf2image import convert_from_bytes

# Configure the API key
Api_key = 'API_KEY'
genai.configure(api_key=Api_key)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input,image, prompt):
    # Generates content using the model directly with the PIL Image
    response = model.generate_content([input,image,prompt])
    return response.text

def pdf_to_image(pdf_file):

    #Convert the first page of a PDF file to a PIL Image object.

    images = convert_from_bytes(pdf_file.read())
    if images:
        return images[0]  # Returns the first page
    else:
        raise ValueError("No pages found in the PDF.")

def main():
    st.title("Invoice Information Extractor")

    st.write("Upload a PDF invoice to extract information.")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])


    if uploaded_file is not None:
        # Convert the first page of the PDF to an image
        image = pdf_to_image(uploaded_file)
        
        # Display the image
        st.image(image, caption="First Page of the Invoice", use_column_width=True)
        # Define the input prompt 
         input_prompt = """act as an expert in extracting information from invoices.response with revelant answers for the questions asked based on the invoice."""
        # Input prompt
        prompt = st.text_input("Enter your prompt:", "Extract key details from this invoice.")

        if st.button("Extract Information"):
            # Get the response from the model
            response_text = get_gemini_response(input_prompt,image, prompt)
            st.write("**Extracted Information:**")
            st.write(response_text)

if __name__ == "__main__":
    main()