import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Simulador de Plantio de Soja", layout="centered")

# Título
st.title("🌱 Simulador de Alocação de Plantio de Soja")

st.markdown("""
Este simulador ajuda a estimar a viabilidade de alocar um multiplicador para o plantio de soja.
Preencha os dados abaixo para obter a recomendação.
""")

# Entradas do simulador
apelo_regional = st.slider("Apelo Regional", 0, 10, 5)
paridade_total = st.slider("Paridade Total", 0, 10, 5)
dispersao = st.selectbox("Dispersão Temporal e Espacial", ["Baixa", "Média", "Alta"])
qualidade_input = st.number_input("Histórico de Qualidade (%)", min_value=0.0, max_value=100.0, value=90.0)
local_venda = st.selectbox("Local de Venda do Produto", ["Sul", "Sudeste", "Centro-Oeste", "Norte", "Nordeste"])
epoca_plantio = st.selectbox("Época de Plantio", ["Verão cedo", "Normal", "Tardio", "Inverno"])
limite_volume_input = st.number_input("Limite de Volume do Multiplicador (%)", min_value=0.0, max_value=100.0, value=18.0)
volume_tratado = st.number_input("% de Volume que será Tratado na Safra", min_value=0.0, max_value=100.0, value=80.0)
historico_entrega_input = st.selectbox("Histórico de Entrega", ["Confiável", "Regular", "Inconstante"])
capacidade_input = st.number_input("Capacidade Nominal Requerida (ha)", min_value=0.0, value=120.0)

# Base fictícia de multiplicadores
dados = {
    "Multiplicador": ["João Silva", "Maria Terra", "Agro Forte", "Plantar Bem", "Campo Rico"],
    "Região": ["Sul", "Norte", "Centro-Oeste", "Sudeste", "Sul"],
    "Capacidade": [120, 80, 150, 100, 90],
    "Qualidade (%)": [92, 88, 85, 90, 95],
    "Entrega": ["Confiável", "Regular", "Confiável", "Inconstante", "Confiável"],
    "Época": ["Normal", "Tardio", "Verão cedo", "Inverno", "Normal"],
    "Yield": [62, 55, 65, 58, 64],
    "LimiteVolume (%)": [18, 22, 19, 21, 17],
    "Cultivar": ["BRS 1010 IPRO", "NS 5959 RR", "TMG 7062", "BS 257", "BRS 1010 IPRO"]
}
df = pd.DataFrame(dados)

# Função para calcular pontuação dos multiplicadores
def calcular_pontuacao(row):
    score = 0
    if row["Região"] == local_venda:
        score += 2
    if row["Época"] == epoca_plantio:
        score += 2
    if row["Qualidade (%)"] >= qualidade_input:
        score += 2
    if row["Entrega"] == historico_entrega_input:
        score += 2
    if row["Capacidade"] >= capacidade_input:
        score += 2
    if row["LimiteVolume (%)"] <= limite_volume_input:
        score += 2
    return score

# Simulação
if st.button("Simular Alocação"):
    df["Pontuação"] = df.apply(calcular_pontuacao, axis=1)
    melhor = df.sort_values(by="Pontuação", ascending=False).iloc[0]

    st.markdown(f"""
    ### 🔍 Melhor Multiplicador Encontrado: **{melhor['Multiplicador']}**
    - 📈 Yield Estimado: **{melhor['Yield']} sc/ha**
    - 🌿 Cultivar Recomendada: **{melhor['Cultivar']}**
    - 🧮 Pontuação Total: **{melhor['Pontuação']} pontos**
    """)
