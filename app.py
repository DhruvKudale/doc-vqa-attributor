import streamlit as st
import pandas as pd
from main import get_attributed_image

st.write("Get Attribution from LLM Answer")

uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
answer = st.text_input(label= "Enter LLM answer here", value="", )
if len(answer) and len(uploaded_file.name):
    final_image = get_attributed_image(pdf_path = uploaded_file.name, answer = answer)
    st.image(final_image)