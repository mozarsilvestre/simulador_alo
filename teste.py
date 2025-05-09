import streamlit as st

# Configuração da página
st.set_page_config(page_title="Simulador de Plantio de Soja", layout="centered")

# Título
st.title("🌱 Simulador de Alocação de Plantio de Soja")

st.markdown("""
Este simulador ajuda a estimar a viabilidade de alocar um multiplicador para o plantio de soja.
Preencha os dados abaixo para obter a recomendação.
""")

# Entradas do simulador
multiplicador = st.text_input("Nome ou Código do Multiplicador")
apelo_regional = st.slider("Apelo Regional", 0, 10, 5)
paridade_total = st.slider("Paridade Total", 0, 10, 5)
dispersao = st.selectbox("Dispersão Temporal e Espacial", ["Baixa", "Média", "Alta"])
qualidade = st.number_input("Histórico de Qualidade (%)", min_value=0.0, max_value=100.0, value=90.0)
local_venda = st.selectbox("Local de Venda do Produto", ["Sul", "Sudeste", "Centro-Oeste", "Norte", "Nordeste"])
epoca_plantio = st.selectbox("Época de Plantio", ["Verão cedo", "Normal", "Tardio", "Inverno"])
yield_regional = st.number_input("Yield do Material por Região (sc/ha)", min_value=0.0, value=60.0)
limite_volume = st.number_input("Limite de Volume do Multiplicador (%)", min_value=0.0, max_value=100.0, value=18.0)
volume_tratado = st.number_input("% de Volume que será Tratado na Safra", min_value=0.0, max_value=100.0, value=80.0)
historico_entrega = st.selectbox("Histórico de Entrega", ["Confiável", "Regular", "Inconstante"])
capacidade_nominal = st.number_input("Capacidade Nominal do Multiplicador (ha)", min_value=0.0, value=120.0)

# Simulação
if st.button("Simular Alocação"):
    # Regras genéricas para exemplo
    viavel = qualidade > 85 and historico_entrega == "Confiável" and limite_volume <= 20
    yield_estimado = yield_regional * (1 + (apelo_regional + paridade_total - 10) * 0.01)

    # Cultivar fictícia baseada em época de plantio
    if epoca_plantio == "Verão cedo":
        cultivar = "BRS 1010 IPRO"
    elif epoca_plantio == "Normal":
        cultivar = "TMG 7062"
    elif epoca_plantio == "Tardio":
        cultivar = "NS 5959 RR"
    else:
        cultivar = "BS 257"

    status = "Viável" if viavel else "Precisa Ajustes"

    st.markdown(f"""
    ### 📌 Multiplicador Avaliado: **{multiplicador}**
    - 📈 Yield Estimado: **{yield_estimado:.2f} sc/ha**
    - 🌿 Cultivar Recomendada: **{cultivar}**
    - ✅ Status da Alocação: **{status}**
    """)
