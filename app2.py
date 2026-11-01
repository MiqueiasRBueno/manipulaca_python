import streamlit as st

st.title("Cadastro de Fornecedores")
with st.form("form_fornecedor"):
    st.subheader("Informações Principais")
    razao_social = st.text_input("Razão Social:")
    nome_fantasia = st.text_input("Nome Fantasia:")

    col1, col2 = st.columns(2)

    with col1:
        cnpj = st.text_input("CNPJ:")
    with col2:
        inscricao_estadual = st.text_input("Inscrição Estadual:")

    col3, col4 = st.columns(2)
    with col3:
        telefone = st.text_input("Telefone:")
    with col4:
        email = st.text_input("E-mail:")

    col5, col6 = st.columns(2)    
    with col5:
        rua = st.text_input("Rua:")
    with col6:
        complemento = st.text_input("Complemento:")

    col7, col8, col9 = st.columns(3)
    with col7:
        cidade = st.text_input("Cidade:")
    with col8:
        estado = st.selectbox("Estado", ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO",
                                   "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", 
                                   "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"])
    with col9:
        cep = st.text_input("CEP:")    
    isento = st.checkbox("Isento")
    salvar = st.form_submit_button("Salvar")

if salvar:
    st.write("Fornecedor: ", razao_social)
    st.write("Nome Fantasia: ", nome_fantasia)
    st.write("CNPJ: ", cnpj)
    st.write("Inscrição Estadual: ", inscricao_estadual)
    st.write("Telefone: ")
    st.write("E-mail: ")
    st.write("Rua: ", rua)
    st.write("Complemento: ", complemento)
    st.write("Cidade: ", cidade)
    st.write("Estado: ", estado)
    st.write("CEP:", cep)
    st.write("Isento: ", isento)
