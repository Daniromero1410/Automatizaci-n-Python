import streamlit as st

#Front
st.image('assets/combine-pdf.png')
st.header('Unir PDF')
st.subheader('Adjuntar Pdfs para unir')

pdf_adjuntos = st.file_uploader(label="",accept_multiple_files=True)

unir = st.button(label="Unir PDFS") #Crea un boton llamado "Unir PDf"
