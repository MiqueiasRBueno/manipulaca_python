import streamlit as st
import re
import csv
from pathlib import Path
import pandas as pd

arquivo_csv = Path("fornecedores.csv")

def salvar_fornecedor(dados):
    criar_cabecalho = (
        not arquivo_csv.exists()
        or arquivo_csv.stat().st_size == 0
    )
    with arquivo_csv.open(
        mode="a", newline="", encoding="utf-8"
    ) as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=dados.keys(), quoting=csv.QUOTE_NONNUMERIC)
        if criar_cabecalho:
            escritor.writeheader()
        escritor.writerow(dados)

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

    col5, col6, col7 = st.columns(3)    
    with col5:
        logradouro = st.selectbox("Logradouro", [
    "Rua", "Avenida", "Praça", "Travessa", "Alameda", "Estrada"])
    with col6:
        endereco = st.text_input("Endereço:")
    with col7:
        complemento = st.text_input("Complemento:")

    col8, col9, col10 = st.columns(3)
    with col8:
        cidade = st.text_input("Cidade:")
    with col9:
        estado = st.selectbox("Estado", ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO",
                                   "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", 
                                   "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"])
    with col10:
        cep = st.text_input("CEP:")    
    isento = st.checkbox("Isento")
    salvar = st.form_submit_button("Salvar")

cnpj_limpo = re.sub(r"\D", "", cnpj)

if salvar:
    if not razao_social.strip():
        st.error("Informe a Razão Social.")
    elif not cnpj.strip():
        st.error("Informe o Cnpj.")
    elif len(cnpj_limpo) != 14:
        st.error("O CNPJ deve conter 14 números.")
    elif not inscricao_estadual.strip():
        st.error("Informe a inscrição estadual.")
    elif not telefone.strip():
        st.error("Informe o telefone para contado.")
    elif not email.strip():
        st.error("Informe o e-mail principal.")
    elif not endereco.strip():
        st.error("Informe o endereço.")
    else:        
        fornecedor = {
            "razao_social": razao_social.strip(),
            "nome_fantasia": nome_fantasia.strip(),
            "cnpj": cnpj_limpo,
            "Inscrição Estadual": inscricao_estadual,
            "Telefone": telefone,
            "E-mail": email,
            "Logradouro": logradouro,
            "Endereço": endereco,
            "Complemento": complemento,
            "Cidade": cidade,
            "Estado": estado,
            "Cep": cep,
            "isento": str(isento)
        }
        salvar_fornecedor(fornecedor)
        st.success("Dados validados com sucesso!")

st.subheader("Fornecedores Cadastrados")
if arquivo_csv.exists() and arquivo_csv.stat().st_size > 0:
    df = pd.read_csv(
        arquivo_csv, dtype=str, keep_default_na=False
    )
    st.dataframe(df, use_container_width=True)
else:
    st.info("Nenhum fornecedor cadastrado.")
