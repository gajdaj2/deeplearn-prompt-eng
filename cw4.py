import streamlit as st
import time

st.title('Przykład Streamlit ze Spinnerem')

with st.spinner('Czekaj... Trwa ładowanie danych'):
    # Symulacja długotrwałej operacji
    time.sleep(5)

st.success('Dane zostały załadowane!')

