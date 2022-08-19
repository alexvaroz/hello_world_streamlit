import streamlit as st

st.title("Minha primeira aplicação")

st.markdown("#### Minha primera aplicação realizará uma contagem de palavras em um texto fornecido.")
text = st.text_input("")
number_words = len(text.split(" "))
if number_words > 1:
    st.write(" O texto digitado possui ", number_words, " palavras.")

st.sidebar.header("About")
st.sidebar.subheader("Essa aplicação foi desenvolvida por Alexandre Vaz")
