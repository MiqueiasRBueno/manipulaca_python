import streamlit as st

st.title("Sistema de Gestão de Fornecedores")
st.header("Cadastro de Empresas")
st.subheader("Informação Cadastrais")
st.write("Aplicação desenvolvida utilizando Python e Streamlit")

st.markdown("**Cadastro de Fornecedores**")
st.markdown("*Gerenciamento de infromações empresariai*")
st.caption("Sistema desenvolvido para fins acadêmicos")
st.text("Versão 1.0")
st.code("print('Olá, Streanlit!')", language="python")
st.markdown("[Link para a documentação oficial Streamlit](https://docs.streamlit.io/)")

st.info("Preencha os dados para realizar um cadastro.")
st.success("Operação realizado com sucesso!")
st.warning("Algumas informações aina não foram preenchidas.")
st.error("Não foi possível concluir a operação.")

st.metric(
    label="Fornecedores Cadastrados",
    value=25,
    delta=5
)

with st.container(border=True):
    st.subheader("Informações do Sistema")
    st.write("Módulo de Cadastro de Fornecedores")
    st.write("Armazenamento em arquive CSV")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Dados Cadastrais")
    st.write("Razão Social")
    st.write('CNPJ')

with col2:
    st.subheader("Dados de Contrato")
    st.write("Telefone")
    st.write("E-mail")

col1, col2 = st.columns([3, 1])
with col1:
    st.write("Nome da Empresa")
with col2:
    st.write("Código")

st.divider()
with st.expander("Sobre o Sistema"):
    st.write(
        "Está aplicação permite cadastrar fornecedores "
        "e armazenar suas informações em arquivo CSV"
    )

razao_social = st.text_input("Razão Social")
nome_fantazia = st.text_input("Nome Fantazia")
st.write("Razão Social informada: ", razao_social)
st.write("Nome Fantasia informado: ", nome_fantazia)

estado =  st.selectbox("Estado", ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO",
                                   "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", 
                                   "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"])
isento = st.checkbox("Isento de Inscrição Estadual")
st.write("Estado selecionado: ", estado)
st.write("Isento: ", isento)

nome = st.text_input("Nome do Fornecedor")
if st.button("Confirmar"):
    st.success(f"Fornecedor {nome} confirmado!")