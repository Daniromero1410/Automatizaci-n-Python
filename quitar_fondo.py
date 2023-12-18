import streamlit as st

st.header("Background Removal App")
st.subheader("Upload an image")
uploaded_image = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    st.image(uploaded_image,caption="Imagen Subida",use_column_width=True)

    remove_button = st.button(label="Quitar Fondo")
