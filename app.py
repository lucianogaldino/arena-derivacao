import streamlit as st
import sympy as sp
import re

# -------------------------------------------------
# CONFIGURAÇÃO INICIAL
# -------------------------------------------------
st.set_page_config(page_title="Guardiões da Taxa de Variação", page_icon="⚔️")

st.title("⚔️ Guardiões da Taxa de Variação")

# -------------------------------------------------
# ESTADO DA MISSÃO
# -------------------------------------------------
if "fase" not in st.session_state:
    st.session_state.fase = 1

# -------------------------------------------------
# FUNÇÃO PARA NORMALIZAR EXPRESSÃO DO ALUNO
# -------------------------------------------------
def normalizar(expr):
    expr = expr.replace("^", "**")
    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)
    expr = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', expr)
    return expr

# -------------------------------------------------
# BARRA LATERAL
# -------------------------------------------------
st.sidebar.title("📊 Progresso da Missão")
st.sidebar.progress(st.session_state.fase / 3)
st.sidebar.write(f"Fase atual: {st.session_state.fase}/3")

if st.sidebar.button("🔄 Reiniciar Missão"):
    st.session_state.fase = 1
    st.rerun()

# -------------------------------------------------
# FASE 1
# -------------------------------------------------
if st.session_state.fase == 1:

    st.header("🧪 Fase 1 — O Reator de Chronópolis")

    st.markdown("""
    A cidade futurista **Chronópolis** depende de um reator experimental.

    A energia liberada é descrita por:

    ### 🔋 E(t) = 6t⁴ − 3t² + 8t

    Para estabilizar o núcleo, você precisa determinar a  
    **taxa de variação instantânea da energia em relação ao tempo t**.

    Se errar, o reator ficará instável!
    """)

    t = sp.symbols('t')
    funcao = 6*t**4 - 3*t**2 + 8*t
    resposta_correta = sp.diff(funcao, t)

    resposta_usuario = st.text_input("Digite a taxa de variação:")

    if resposta_usuario:
        try:
            resposta_formatada = normalizar(resposta_usuario)
            resposta_usuario_expr = sp.sympify(resposta_formatada)

            if sp.simplify(resposta_usuario_expr - resposta_correta) == 0:
                st.success("🔥 Reator estabilizado! Chronópolis está salva!")

                if st.button("➡️ Avançar para Fase 2"):
                    st.session_state.fase = 2

            else:
                st.error("⚠️ Instabilidade detectada! Revise seus cálculos.")

        except:
            st.error("Formato inválido! Use apenas expressões matemáticas.")

# -------------------------------------------------
# FASE 2
# -------------------------------------------------
elif st.session_state.fase == 2:

    st.header("🚀 Fase 2 — Propulsão Orbital")

    st.markdown("""
    Uma nave interplanetária precisa ajustar sua trajetória.

    A posição é dada por:

    ### 🛰️ S(v) = 5v³ − 2v² + 4v

    Para ativar os propulsores, determine a  
    **taxa de variação da posição em relação à variável v**.
    """)

    v = sp.symbols('v')
    funcao = 5*v**3 - 2*v**2 + 4*v
    resposta_correta = sp.diff(funcao, v)

    resposta_usuario = st.text_input("Digite a taxa de variação:")

    if resposta_usuario:
        try:
            resposta_formatada = normalizar(resposta_usuario)
            resposta_usuario_expr = sp.sympify(resposta_formatada)

            if sp.simplify(resposta_usuario_expr - resposta_correta) == 0:
                st.success("🚀 Propulsão ativada! A nave escapou da órbita!")

                if st.button("➡️ Avançar para Fase 3"):
                    st.session_state.fase = 3

            else:
                st.error("❌ Falha nos motores! Revise sua taxa de variação.")

        except:
            st.error("Formato inválido! Use apenas expressões matemáticas.")

# -------------------------------------------------
# FASE 3
# -------------------------------------------------
elif st.session_state.fase == 3:

    st.header("🌋 Fase 3 — O Vulcão da Energia Crescente")

    st.markdown("""
    Um vulcão energético está acumulando pressão.

    A intensidade da pressão é modelada por:

    ### 🌋 P(r) = 7r⁵ − 4r³ + 2r

    Para prever a explosão, calcule a  
    **taxa de variação da pressão em relação à variável r**.

    O destino da civilização depende de você!
    """)

    r = sp.symbols('r')
    funcao = 7*r**5 - 4*r**3 + 2*r
    resposta_correta = sp.diff(funcao, r)

    resposta_usuario = st.text_input("Digite a taxa de variação:")

    if resposta_usuario:
        try:
            resposta_formatada = normalizar(resposta_usuario)
            resposta_usuario_expr = sp.sympify(resposta_formatada)

            if sp.simplify(resposta_usuario_expr - resposta_correta) == 0:
                st.success("🏆 MISSÃO CONCLUÍDA! Você é um Guardião da Taxa de Variação!")
                st.balloons()

            else:
                st.error("🌋 A pressão aumentou! Revise seus cálculos.")

        except:
            st.error("Formato inválido! Use apenas expressões matemáticas.")
