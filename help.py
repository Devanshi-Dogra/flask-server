import pdfplumber
import pytesseract
from PIL import Image
from transformers import pipeline

summarization_model = pipeline("summarization", model="facebook/bart-large-cnn")

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        # return("text dummy")
        return "".join(page.extract_text() for page in pdf.pages)

def extract_text_from_image(file):
    image = Image.open(file)
    # return("text dummy")
    return pytesseract.image_to_string(image)

def generate_summary(text, length="medium"):
    max_len = {"short": 500, "medium": 1000, "long": 2000}[length]
    return summarization_model(text, max_length=max_len, min_length=25, do_sample=False)[0]["summary_text"]
