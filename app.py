import streamlit as st
import sympy as sp
import re

from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application
)

# -------------------------------------------------
# CONFIGURAÇÃO
# -------------------------------------------------
st.set_page_config(page_title="Guardiões da Taxa de Variação", page_icon="⚔️")
st.title("⚔️ Guardiões da Taxa de Variação — Nível Avançado")

if "fase" not in st.session_state:
    st.session_state.fase = 1

# -------------------------------------------------
# PARSER ROBUSTO (ACEITA TEXTO PLANO NATURAL)
# -------------------------------------------------
def interpretar(expr):
    expr = expr.lower()
    expr = expr.replace("^", "**")
    expr = expr.replace("sen", "sin")

    transformations = standard_transformations + (
        implicit_multiplication_application,
    )

    return parse_expr(expr, transformations=transformations)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
st.sidebar.title("📊 Progresso")
st.sidebar.progress(st.session_state.fase / 5)
st.sidebar.write(f"Fase {st.session_state.fase} de 5")

if st.sidebar.button("🔄 Reiniciar Missão"):
    st.session_state.fase = 1
    st.rerun()

# =================================================
# FASE 1 — DEFINIÇÃO
# =================================================
if st.session_state.fase == 1:

    st.header("🧪 Fase 1 — Núcleo Fundamental")

    st.markdown("""
    O reator central precisa de calibração manual.

    ### E(t) = t³ − 2t² + 5t − 7

    Calcule a **taxa de variação usando a definição formal**.
    """)

    t = sp.symbols('t')
    funcao = t**3 - 2*t**2 + 5*t - 7
    resposta_correta = sp.diff(funcao, t)

    resposta = st.text_input("Digite a taxa de variação:")

    if resposta:
        try:
            resp = interpretar(resposta)
            if sp.simplify(resp - resposta_correta) == 0:
                st.success("🔥 Núcleo ativado!")
                if st.button("➡️ Fase 2"):
                    st.session_state.fase = 2
            else:
                st.error("❌ Revise a definição.")
        except:
            st.error("Formato inválido.")

# =================================================
# FASE 2 — PRODUTO
# =================================================
elif st.session_state.fase == 2:

    st.header("⚙️ Fase 2 — Engrenagens Trigonométricas")

    st.markdown("""
    ### F(x) = (x² + 1) sin(x)

    Calcule a **taxa de variação usando a regra do produto**.
    """)

    x = sp.symbols('x')
    funcao = (x**2 + 1)*sp.sin(x)
    resposta_correta = sp.diff(funcao, x)

    resposta = st.text_input("Digite a taxa de variação:")

    if resposta:
        try:
            resp = interpretar(resposta)
            if sp.simplify(resp - resposta_correta) == 0:
                st.success("⚙️ Engrenagens estabilizadas!")
                if st.button("➡️ Fase 3"):
                    st.session_state.fase = 3
            else:
                st.error("❌ Revise a regra do produto.")
        except:
            st.error("Formato inválido.")

# =================================================
# FASE 3 — QUOCIENTE
# =================================================
elif st.session_state.fase == 3:

    st.header("🌊 Fase 3 — Fluxo Exponencial")

    st.markdown("""
    ### Q(y) = e^y / (y² + 1)

    Calcule a **taxa de variação usando a regra do quociente**.
    """)

    y = sp.symbols('y')
    funcao = sp.exp(y)/(y**2 + 1)
    resposta_correta = sp.diff(funcao, y)

    resposta = st.text_input("Digite a taxa de variação:")

    if resposta:
        try:
            resp = interpretar(resposta)
            if sp.simplify(resp - resposta_correta) == 0:
                st.success("🌊 Fluxo estabilizado!")
                if st.button("➡️ Fase 4"):
                    st.session_state.fase = 4
            else:
                st.error("❌ Revise a regra do quociente.")
        except:
            st.error("Formato inválido.")

# =================================================
# FASE 4 — CADEIA
# =================================================
elif st.session_state.fase == 4:

    st.header("🧬 Fase 4 — Reação Composta")

    st.markdown("""
    ### R(z) = cos(3z² + 2z)

    Calcule a **taxa de variação usando a regra da cadeia**.
    """)

    z = sp.symbols('z')
    funcao = sp.cos(3*z**2 + 2*z)
    resposta_correta = sp.diff(funcao, z)

    resposta = st.text_input("Digite a taxa de variação:")

    if resposta:
        try:
            resp = interpretar(resposta)
            if sp.simplify(resp - resposta_correta) == 0:
                st.success("🧬 Reação controlada!")
                if st.button("➡️ Fase 5"):
                    st.session_state.fase = 5
            else:
                st.error("❌ Revise a regra da cadeia.")
        except:
            st.error("Formato inválido.")

# =================================================
# FASE 5 — COMBINAÇÃO FINAL
# =================================================
elif st.session_state.fase == 5:

    st.header("🔥 Fase Final — Sistema Supremo")

    st.markdown("""
    ### S(w) = [(w² + 1) e^w] / sin(w)

    Combine:
    - Produto
    - Quociente
    - Cadeia

    Calcule a **taxa de variação completa**.
    """)

    w = sp.symbols('w')
    funcao = ((w**2 + 1)*sp.exp(w))/sp.sin(w)
    resposta_correta = sp.diff(funcao, w)

    resposta = st.text_input("Digite a taxa de variação final:")

    if resposta:
        try:
            resp = interpretar(resposta)
            if sp.simplify(resp - resposta_correta) == 0:
                st.success("🏆 MISSÃO COMPLETA! Você domina cálculo avançado!")
                st.balloons()
            else:
                st.error("❌ O sistema ainda não está estável.")
        except:
            st.error("Formato inválido.")
