import streamlit as st

# Inicializar el estado de sesión
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

# BOTONES:
if st.button("Haz clic aquí"):
    st.session_state.button_clicked = True

# Mostrar el mensaje si el botón fue presionado
if st.session_state.button_clicked:
    st.write("¡Botón presionado!")

# ENTRADA DE TEXTO:
name = st.text_input("¿Cómo te llamas?")
if name:
    st.write(f"Hola, {name}!")

