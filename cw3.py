import streamlit as st

st.title('Wybór z rozwijanej listy')

option = st.selectbox(
    'Jakie jest Twoje ulubione zwierzę?',
    ('Pies', 'Kot', 'Królik', 'Papuga')
)

st.write('Twoje ulubione zwierzę to:', option)
