import streamlit as st

st.title("Cadastro de Fornecedores")
with st.form("form_fornecedor"):
    st.subheader("Informaçôes Princcipais")
    razao_social = st.text_input("Razão Social")
    nome_fantasia = st.text_input("Nome Fantasia")
    col1, col2 = st.columns(2)
    with col1:
        cnpj = st.text_input("CNPJ")
    with col2:
        inscricao_estadual = st.text_input("Inscrição Estadual")
    isento = st.checkbox("Isento")
    salvar = st.form_submit_button("Salvar")

if salvar:
    st.write("Fornecedor: ", razao_social)
    st.write("Nome Fantasia: ", nome_fantasia)
    st.write("CNPJ: ", cnpj)
    st.write("Inscrição Estadual: ", inscricao_estadual)
    st.write("Isento: ", isento)
