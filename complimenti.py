import streamlit as st
import time

# Configurazione della pagina
st.set_page_config(page_title="SORPRESA PER ENRICO", page_icon="🎂", layout="centered")

# CSS per rendere tutto molto colorato e assurdo
st.markdown("""
    <style>
    .main { background-color: #000000; }
    .titolo-pazzo {
        color: #FF00FF;
        font-size: 70px !important;
        text-align: center;
        font-weight: bold;
        text-shadow: 4px 4px #39FF14;
    }
    .testo-offesa {
        color: #FFFFFF;
        font-size: 25px;
        text-align: center;
        line-height: 1.6;
        border: 2px solid #39FF14;
        padding: 20px;
        border-radius: 15px;
    }
    .prezzi {
        color: #39FF14;
        font-weight: bold;
        font-size: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# Pagina Iniziale
st.markdown('<p class="titolo-pazzo">AUGURI ENRICO! 🎈</p>', unsafe_allow_html=True)
st.write("")

if 'cliccato' not in st.session_state:
    st.session_state.cliccato = False

def clicca():
    st.session_state.cliccato = True

if not st.session_state.cliccato:
    st.warning("⚠️ ATTENZIONE: Questo messaggio contiene una sorpresa speciale solo per Enrico.")
    st.button("CLICCA PER APRIRE IL REGALO 🎁", on_click=clicca)
else:
    # Effetto caricamento per creare ansia
    with st.spinner('Analizzando il livello di bruttezza...'):
        time.sleep(2)
    
    # Esplosione di effetti
    st.balloons()
    st.snow()
    
    # Il Messaggio
    st.markdown('<p class="titolo-pazzo">MA COMUNQUE...</p>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="testo-offesa">
            Sei proprio un <b>BRUTTO GAY</b>, te lo dovevo dire.<br><br>
            Mi ricordo ancora quando eri nato... <br>
            Ti volevano <b>buttar giù dalle scale</b> perché eri troppo brutta, 
            una roba inguardabile! 🤮
        </div>
        """, unsafe_allow_html=True)
    
    st.write("")
    st.write("---")
    
    # Sezione Mamma
    st.markdown('<p style="text-align:center; font-size:40px;">💰</p>', unsafe_allow_html=True)
    st.error("DOMANDA IMPORTANTE:")
    st.markdown(f"""
        <div style="text-align: center;">
            <p class="prezzi">Mi dici i prezzi di Valeria tua mamma??</p>
            <p style="color: grey;">Gli amici vorrebbero sapere il listino aggiornato 2024/2025.</p>
        </div>
        """, unsafe_allow_html=True)

    # Immagine random divertente
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJic2ZqZzRyeG53eXN6eHByeG53eXN6eHByeG53eXN6eHByeG53eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0MYt5jPR6QX5pnqM/giphy.gif")

    if st.button("RIVEDILO ANCORA 🌈"):
        st.balloons()
