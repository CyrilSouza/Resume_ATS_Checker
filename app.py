import streamlit as st
import google.generativeai as genai   
import os
import PyPDF2 as pdf


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def input_pdf_txt(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):  
        page = reader.pages[page]
        text += str(page.extract_text())  
    return text

input_prompt = """
Hey Act like a skilled or very experienced ATS (Application Tracking System) with a deep understanding of the tech field,
software engineering, data science, data analyst, big data engineer, Frontend Engineer, and UI/UX Engineer. 
Provide a job description for a position in the tech field, such as software engineering, data science, data analysis, big data engineering, frontend engineering, or UI/UX engineering. Then, upload a PDF resume, and I'll evaluate it based on the given job description. I'll assign a percentage match based on how well the resume aligns with the job description, and I'll identify missing keywords with high accuracy
resume: {text}
description: {jd}

I want the response in one single string having the structure
JD Match: %

Missing Keywords : []

Profile Summary : ""
"""

st.title("©️ Connect-Verse ATS")
st.text("Improve Your Resume ATS")
jd = st.text_area("Paste the Job Description here")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")
submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        with st.spinner("Processing..."):
            text = input_pdf_txt(uploaded_file)
            response = get_gemini_response(input_prompt.format(text=text, jd=jd))
            st.subheader(response)
