import streamlit as st
import time

# Configurazione pagina
st.set_page_config(page_title="Messaggio Speciale", page_icon="🎉")

# Funzione per l'effetto coriandoli (utilizza HTML/JS per un effetto immediato)
def celebrate():
    st.balloons() # Effetto palloncini nativo di Streamlit
    st.snow()     # Effetto neve (che sembrano stelline/coriandoli bianchi)

# Titolo principale con stile
st.markdown("""
    <style>
    .main-title {
        font-size: 50px;
        font-weight: bold;
        color: #FF4B4B;
        text-align: center;
        margin-top: 20%;
    }
    </style>
    """, unsafe_allow_html=True)

# Visualizzazione del messaggio
st.markdown('<p class="main-title">🌟 ENRICO È UN BRUTTO GAYY!! 🌟</p>', unsafe_allow_html=True)

# Attiva l'animazione al caricamento
celebrate()

# Aggiunge un tocco di "coriandoli" extra con un messaggio di testo
st.write("✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
