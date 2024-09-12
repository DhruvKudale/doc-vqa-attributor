import streamlit as st
import os
from main import get_attributed_image
input_dir = 'documents/'

def save_uploaded_file(uploadedfile):
    with open(os.path.join(input_dir, uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success("Saved File:{} to tempDir".format(uploadedfile.name))

st.write("Get Attribution from LLM Answer")

uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
answer = st.text_input(label= "Enter LLM answer here", value="", )
if len(answer) and len(uploaded_file.name):
    save_uploaded_file(uploaded_file)
    pdf_path = input_dir + uploaded_file.name
    final_image = get_attributed_image(pdf_path = pdf_path, answer = answer)
    st.image(final_image)