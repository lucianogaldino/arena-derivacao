import streamlit as st
import sympy as sp
import re

# -----------------------------
# Configuração inicial
# -----------------------------
st.set_page_config(page_title="Missão: Guardiões da Taxa de Variação", page_icon="⚔️")

st.title("⚔️ Missão: Guardiões da Taxa de Variação")

# -----------------------------
# Sistema de fases
# -----------------------------
if "fase" not in st.session_state:
    st.session_state.fase = 1

# -----------------------------
# Função para normalizar entrada
# -----------------------------
def normalizar(expr):
    expr = expr.replace("^", "**")
    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)
    expr = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', expr)
    return expr

# -----------------------------
# FASE 1
# -----------------------------
if st.session_state.fase == 1:

    st.header("🧪 Fase 1 — O Reator de Energia Temporal")

    st.markdown("""
    A cidade futurista de **Chronópolis** está sendo abastecida por um reator experimental.
    
    A energia liberada pelo núcleo é descrita pela função:

    ### 🔋 E(t) = 6t⁴ - 3t² + 8t

    Para estabilizar o reator, você precisa determinar a **taxa de variação instantânea da energia**.

    ⚠️ Se errar, o núcleo ficará instável!
    
    Digite abaixo a taxa de variação da energia em relação ao tempo t:
    """)

    t = sp.symbols('t')
    funcao = 6*t**4 - 3*t**2 + 8*t
    resposta_correta = sp.diff(funcao, t)

    resposta_usuario = st.text_input("Sua resposta:")

    if resposta_usuario:
        try:
            resposta_formatada = normalizar(resposta_usuario)
            resposta_usuario_expr = sp.sympify(resposta_formatada)

            if sp.simplify(resposta_usuario_expr - resposta_correta) == 0:
                st.success("🔥 Reator estabilizado! Você salvou Chronópolis!")
                st.session_state.fase = 2
                st.rerun()
            else:
                st.error("⚠️ Instabilidade detectada! Revise seus cálculos.")
        except:
            st.error("Formato inválido! Use apenas expressões matemáticas.")

# -----------------------------
# FASE 2
# -----------------------------
elif st.session_state.fase == 2:

    st.header("🚀 Fase 2 — A Nave de Propulsão Variável")

    st.markdown("""
    Uma nave interplanetária precisa ajustar sua aceleração para escapar da órbita de um planeta.

    A posição da nave é dada por:

    ### 🛰️ S(v) = 5v³ - 2v² + 4v

    Para ativar o propulsor, é necessário determinar a **taxa de variação da posição em relação à variável v**.

    Calcule essa taxa de variação:
    """)

    v = sp.symbols('v')
    funcao = 5*v**3 - 2*v**2 + 4*v
    resposta_correta = sp.diff(funcao, v)

    resposta_usuario = st.text_input("Sua resposta:")

    if resposta_usuario:
        try:
            resposta_formatada = normalizar(resposta_usuario)
            resposta_usuario_expr = sp.sympify(resposta_formatada)

            if sp.simplify(resposta_usuario_expr - resposta_correta) == 0:
                st.success("🚀 Propulsão ativada! Você escapou da órbita!")
                st.session_state.fase = 3
                st.rerun()
            else:
                st.error("❌ A nave perdeu potência! Revise a taxa de variação.")
        except:
            st.error("Formato inválido! Use apenas expressões matemáticas.")

# -----------------------------
# FASE 3
# -----------------------------
elif st.session_state.fase == 3:

    st.header("🌋 Fase 3 — O Vulcão da Energia Crescente")

    st.markdown("""
    Um vulcão energético está acumulando pressão.

    A intensidade da pressão é modelada por:

    ### 🌋 P(r) = 7r⁵ - 4r³ + 2r

    Para prever a explosão, precisamos calcular a **taxa de variação da pressão em relação à variável r**.

    Se acertar, você salva a civilização próxima!
    """)

    r = sp.symbols('r')
    funcao = 7*r**5 - 4*r**3 + 2*r
    resposta_correta = sp.diff(funcao, r)

    resposta_usuario = st.text_input("Sua resposta:")

    if resposta_usuario:
        try:
            resposta_formatada = normalizar(resposta_usuario)
            resposta_usuario_expr = sp.sympify(resposta_formatada)

            if sp.simplify(resposta_usuario_expr - resposta_correta) == 0:
                st.success("🏆 MISSÃO CONCLUÍDA! Você se tornou um Guardião da Taxa de Variação!")
                st.balloons()
            else:
                st.error("🌋 A pressão aumentou! Revise seus cálculos.")
        except:
            st.error("Formato inválido! Use apenas expressões matemáticas.")

# -----------------------------
# Barra lateral
# -----------------------------
st.sidebar.title("📊 Progresso")
st.sidebar.write(f"Fase atual: {st.session_state.fase}/3")

if st.sidebar.button("🔄 Reiniciar missão"):
    st.session_state.fase = 1
    st.rerun()
