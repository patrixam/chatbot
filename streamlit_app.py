import streamlit as st

# CSS global para cambiar la fuente de los mensajes del chat
st.markdown("""
    <style>
        .stChatMessage {
            font-family: 'Arial', sans-serif;
            font-size: 3px;
            color: #333;
        }
        .stChatMessageUser {
            font-family: 'Courier New', monospace;
            font-size: 5px;
            color: green;
        }
        .stChatMessageAssistant {
            font-family: 'Verdana', sans-serif;
            font-size: 300px !important;
            color: green;
        }
    </style>
""", unsafe_allow_html=True)

# Título de la aplicación
st.title("💬 Chat personalizado en Streamlit")

# Lista para almacenar el historial de chat en la sesión
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes previos del historial
for message in st.session_state.messages:
    role = message["role"]
    with st.chat_message(role):
        st.markdown(
            f"<p class='stChatMessage{role.capitalize()}'>{message['content']}</p>",
            unsafe_allow_html=True
        )

# Input del usuario
user_input = st.chat_input("Escribe tu mensaje aquí...")

if user_input:
    # Guardar y mostrar el mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(
            f"<p class='stChatMessageUser'>{user_input}</p>",
            unsafe_allow_html=True
        )

    # Respuesta automática del asistente
    response = f"🤖 Respondí a: {user_input}"
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(
            f"<p class='stChatMessageAssistant'>{response}</p>",
            unsafe_allow_html=True
        )

