# doc-vqa-attributor

A Streamlit-based tool designed for Document Visual Question Answering (VQA) with attribution. This UI enables users to upload PDF documents and match answers provided by a Language Model (LLM) to specific areas within the document. The final output highlights the relevant text region with a green bounding box in the document image.

## Features

- **PDF Upload**: Easily upload a PDF document to the `documents` folder.
- **LLM Answer Input**: Paste the answer generated by the chatbot or any other source.
- **Attribution**: The tool identifies and highlights the text region in the PDF that corresponds to the provided answer.
- **Interactive UI**: Simple and user-friendly interface built with Streamlit.

## Installation

To run the `doc-vqa-attributor` UI locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/doc-vqa-attributor.git
   cd doc-vqa-attributor

2. **Run the Streamlit app**:

   ```bash
   streamlit run app.py



