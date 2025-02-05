import streamlit as st

#BOTONES:
if st.button("Haz clic aquí"):
   st.write("¡Botón presionado!")

#ENTRADA DE TEXTO:
name = st.text_input("¿Cómo te llamas?")
if name:
    st.write(f"Hola, {name}!")

#DESLIZADORES:
age = st.slider("Selecciona tu edad", 0, 100, 25)
st.write(f"Tienes {age} años")
