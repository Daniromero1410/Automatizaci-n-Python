import streamlit as st
import PyPDF2

#Variables
output_pdf = ("documents/pdf_final.pdf")

#Funciones
def unir_pdfs(output_path,documents):
    pdf_final = PyPDF2.PdfMerger()

    for document in documents:
        pdf_final.append(document)
    pdf_final.write(output_path)

    
#Front
st.image('assets/combine-pdf.png')
st.header('Unir PDF')
st.subheader('Adjuntar Pdfs para unir')

pdf_adjuntos = st.file_uploader(label="",accept_multiple_files=True)

unir = st.button(label="Unir PDFS") #Crea un boton llamado "Unir PDf"
