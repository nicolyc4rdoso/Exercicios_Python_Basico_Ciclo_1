import streamlit as st
st.write("ARMY - Aluguel De Carros")
st.sidebar.title("buick super")
st.sidebar.image("ARMY.png")

carros = ["Buick super","ferrari","chevrolet bel air","Lamborghini","mclaren"]

opçao = st.sidebar.selectbox("escolha o carro que foi alugado", carros)

st.image(f"{opçao}.png")
st.markdown(f"## Você Alugou o Modelo:{opçao}")
st.markdown("---")

dias = st.text_input(f"Por quantos dias o {opçao} foi alugado?")
km = st.text_input(f"quantos km você rodou com o {opçao}?")