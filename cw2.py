import streamlit as st

st.title('Interakcja z użytkownikiem')

name = st.text_input('Podaj swoje imię')
if name:
    st.write(f'Cześć, {name}!')
