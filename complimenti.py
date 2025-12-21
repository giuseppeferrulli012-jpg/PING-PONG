import streamlit as st
import time

# Configurazione della pagina
st.set_page_config(page_title="PER ENRICO", page_icon="🎂")

# CSS aggiornato per visibilità massima
st.markdown("""
    <style>
    .titolo-pazzo {
        color: #FF00FF;
        font-size: 50px !important;
        text-align: center;
        font-weight: bold;
    }
    .box-messaggio {
        background-color: #f0f2f6;
        color: #000000; /* Testo Nero per visibilità */
        font-size: 22px;
        text-align: center;
        padding: 20px;
        border-radius: 15px;
        border: 3px solid #39FF14;
        margin-bottom: 20px;
    }
    .prezzi {
        color: #FF4B4B;
        font-weight: bold;
        font-size: 28px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="titolo-pazzo">AUGURI ENRICO! 🎈</p>', unsafe_allow_html=True)

if 'cliccato' not in st.session_state:
    st.session_state.cliccato = False

if not st.session_state.cliccato:
    if st.button("CLICCA PER IL TUO REGALO 🎁"):
        st.session_state.cliccato = True
        st.rerun()
else:
    # Effetti speciali
    st.balloons()
    
    # Il Messaggio Corretto
    st.markdown("""
        <div class="box-messaggio">
            Comunque sei proprio un <b>BRUTTO GAY</b>, te lo dovevo dire. 🌈<br><br>
            Mi ricordo quando eri nato, che ti volevano <b>buttar giù dalle scale</b> perché era brutta! 🤮
        </div>
        """, unsafe_allow_html=True)
    
    st.write("---")
    
    # Sezione Mamma
    st.markdown('<p class="prezzi">Mi dici i prezzi di Valeria tua mamma?? 💰</p>', unsafe_allow_html=True)
    
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJic2ZqZzRyeG53eXN6eHByeG53eXN6eHByeG53eXN6eHByeG53eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0MYt5jPR6QX5pnqM/giphy.gif")

    if st.button("Rivedi Auguri"):
        st.session_state.cliccato = False
        st.rerun()
