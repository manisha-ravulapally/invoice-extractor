** Invoice Information Extractor**
Objective:

The goal of this project is to build a web application that can extract and analyze information from invoice documents. The application accepts invoice files in PDF format, converts the first page of the PDF into an image, and utilizes a generative AI model to extract key details based on user-provided prompts.

Features:

PDF Upload:  Users can upload an invoice in PDF format using a file uploader widget.
PDF to Image Conversion: The application converts the first page of the uploaded PDF into an image format using the pdf2image library. This ensures that the invoice's content can be processed by image-based models.
Image Display: The extracted image from the first page of the PDF is displayed to the user. This allows users to verify that the correct page has been processed.
Information Extraction: Users can input specific prompts or questions regarding the invoice. The application sends the image and the prompt to a generative AI model (Gemini-1.5-Flash) to extract relevant information.
Response Display: The extracted information is displayed on the web interface, providing users with insights or answers based on the invoice content.
