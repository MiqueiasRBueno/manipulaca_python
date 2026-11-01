import streamlit as st

st.title("Gerenciador de Projetos 📊")
st.write("Navegue pelas abas abaixo para acompanhar os dados:")

# 1. Criando e definindo os nomes das abas
aba_visao_geral, aba_graficos, aba_config = st.tabs([
    "📈 Visão Geral", 
    "📊 Gráficos", 
    "⚙️ Configurações"
])

# 2. Preenchendo a primeira aba (Visão Geral)
with aba_visao_geral:
    st.header("Métricas Principais")
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Tarefas Concluídas", value="42", delta="3")
    col2.metric(label="Projetos Ativos", value="12", delta="-1")
    col3.metric(label="Orçamento Restante", value="R$ 5.400")

# 3. Preenchendo a segunda aba (Gráficos)
with aba_graficos:
    st.header("Análise de Desempenho")
    st.write("Aqui você pode renderizar gráficos do Plotly, Altair ou do próprio Streamlit:")
    
    # Exemplo de gráfico nativo fictício
    dados_ficticios = [10, 20, 15, 30, 25]
    st.line_chart(dados_ficticios)

# 4. Preenchendo a terceira aba (Configurações)
with aba_config:
    st.header("Preferências do Sistema")
    st.checkbox("Ativar notificações por e-mail")
    st.selectbox("Selecione o idioma padrão:", ["Português", "Inglês", "Espanhol"])
    st.button("Salvar Alterações")
