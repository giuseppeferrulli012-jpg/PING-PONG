import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="PaleoRadar v1.0", layout="wide")

st.title("🦖 PaleoRadar: Fossil Finder Simulator")
st.sidebar.header("Parametri di Scansione")

# Controlli interattivi
sensibilita = st.sidebar.slider("Sensibilità Sensore", 0.0, 1.0, 0.7)
profondita = st.sidebar.selectbox("Profondità Scansione", ["Superficiale (0-2m)", "Media (2-10m)", "Profonda (>10m)"])

if st.button("AVVIA SCANSIONE RADAR"):
    with st.spinner('Analisi strati sedimentari in corso...'):
        # Generazione dati simulati
        grid_size = 30
        x = np.linspace(0, 100, grid_size)
        y = np.linspace(0, 100, grid_size)
        X, Y = np.meshgrid(x, y)
        
        # Simuliamo una "firma fossile" basata sulla densità del terreno
        Z = np.sin(X/10) * np.cos(Y/10) + np.random.normal(0, 0.2, (grid_size, grid_size))
        fossili_trovati = Z > (2 - sensibilita * 2)

        # Creazione grafico con Plotly
        fig = px.density_heatmap(
            x=X.flatten(), 
            y=Y.flatten(), 
            z=Z.flatten(),
            color_continuous_scale='Viridis',
            title="Mappa Termica del Sottosuolo"
        )
        
        # Evidenziamo i "Punti di Interesse" (Fossili)
        st.plotly_chart(fig, use_container_width=True)
        
        # Report finale
        count = np.sum(fossili_trovati)
        if count > 0:
            st.success(f"Rilevate {count} anomalie compatibili con resti fossili!")
            
            # Creiamo una tabella con le coordinate delle anomalie
            coords = []
            for i in range(grid_size):
                for j in range(grid_size):
                    if fossili_trovati[i,j]:
                        coords.append({"Lat": 40.8 + (i/1000), "Lon": 16.5 + (j/1000), "Probabilità": f"{np.random.randint(70,99)}%"})
            
            df = pd.DataFrame(coords)
            st.subheader("Coordinate GPS Anomalie")
            st.map(df) # Mostra i punti su una mappa reale (centrata su Altamura come esempio)
            st.table(df)
        else:
            st.warning("Nessuna anomalia rilevata. Prova a cambiare zona o aumentare la sensibilità.")
