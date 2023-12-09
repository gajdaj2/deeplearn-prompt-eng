import streamlit as st

st.title("Generator wizytówki")

name = st.text_input('Podaj swoje imię')
surname = st.text_input('Podaj swoje nazwisko')
profession = st.selectbox("Wybierz zawód", ("Programista", "Tester", "Administrator", "Inny"))
radio = st.radio("Wybierz płeć", ("Mężczyzna", "Kobieta"))


if st.button("Generuj wizytówkę"):
    if name and surname and profession:
        st.write(f"Imię: {name}")
        st.write(f"Nazwisko: {surname}")
        st.write(f"Zawód: {profession}")
        st.write(f"Płeć: {radio}")
    else:
        st.error("Wypełnij wszystkie pola!")
