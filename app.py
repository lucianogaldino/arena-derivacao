import streamlit as st
import sympy as sp
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application
)

# -------------------------------------------------
# CONFIGURAÇÃO DO PARSER
# -------------------------------------------------
transformations = standard_transformations + (implicit_multiplication_application,)

def converter_resposta(resposta):
    resposta = resposta.replace("^", "**")
    return parse_expr(
        resposta,
        transformations=transformations,
        local_dict={"e": sp.E}
    )

# -------------------------------------------------
# CONFIGURAÇÃO GERAL
# -------------------------------------------------
st.set_page_config(page_title="Guardiões da Taxa de Variação", page_icon="⚔️")
st.title("⚔️ Guardiões da Taxa de Variação — Nível Avançado")

if "fase" not in st.session_state:
    st.session_state.fase = 1

if "validado" not in st.session_state:
    st.session_state.validado = False

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
st.sidebar.title("📊 Progresso")
st.sidebar.progress(st.session_state.fase / 5)
st.sidebar.write(f"Fase {st.session_state.fase} de 5")

if st.sidebar.button("🔄 Reiniciar Missão"):
    st.session_state.fase = 1
    st.session_state.validado = False
    st.session_state.clear()
    st.rerun()

# =================================================
# FASE 1
# =================================================
if st.session_state.fase == 1:

    st.header("🧪 Fase 1 — O Núcleo Fundamental")

    st.markdown("""
    ### E(t) = t³ − 2t² + 5t − 7
    Calcule a taxa de variação.
    """)

    t = sp.symbols('t')
    funcao = t**3 - 2*t**2 + 5*t - 7
    resposta_correta = sp.diff(funcao, t)

    resposta = st.text_input("Digite a taxa de variação:", key="fase1")

    if resposta and not st.session_state.validado:
        try:
            resp = converter_resposta(resposta)

            if sp.simplify(resp - resposta_correta) == 0:
                st.success("🔥 Núcleo ativado com sucesso!")
                st.session_state.validado = True
            else:
                st.error("❌ Revise a aplicação da definição.")
        except:
            pass

    if st.session_state.validado:
        if st.button("➡️ Fase 2"):
            st.session_state.fase = 2
            st.session_state.validado = False
            st.session_state["fase1"] = ""
            st.rerun()

# =================================================
# FASE 2
# =================================================
elif st.session_state.fase == 2:

    st.header("⚙️ Fase 2 — Engrenagens Trigonométricas")

    st.markdown("""
    ### F(x) = (x² + 1) · sin(x)
    Calcule usando a regra do produto.
    """)

    x = sp.symbols('x')
    funcao = (x**2 + 1) * sp.sin(x)
    resposta_correta = sp.diff(funcao, x)

    resposta = st.text_input("Digite a taxa de variação:", key="fase2")

    if resposta and not st.session_state.validado:
        try:
            resp = converter_resposta(resposta)

            if sp.simplify(resp - resposta_correta) == 0:
                st.success("⚙️ Engrenagens estabilizadas!")
                st.session_state.validado = True
            else:
                st.error("❌ Revise a regra do produto.")
        except:
            pass

    if st.session_state.validado:
        if st.button("➡️ Fase 3"):
            st.session_state.fase = 3
            st.session_state.validado = False
            st.session_state["fase2"] = ""
            st.rerun()

# =================================================
# FASE 3
# =================================================
elif st.session_state.fase == 3:

    st.header("🌊 Fase 3 — Fluxo Exponencial")

    st.markdown("""
    ### Q(y) = eʸ / (y² + 1)
    Calcule usando a regra do quociente.
    """)

    y = sp.symbols('y')
    funcao = sp.exp(y) / (y**2 + 1)
    resposta_correta = sp.diff(funcao, y)

    resposta = st.text_input("Digite a taxa de variação:", key="fase3")

    if resposta and not st.session_state.validado:
        try:
            resp = converter_resposta(resposta)

            if sp.simplify(resp - resposta_correta) == 0:
                st.success("🌊 Fluxo controlado!")
                st.session_state.validado = True
            else:
                st.error("❌ Revise a regra do quociente.")
        except:
            pass

    if st.session_state.validado:
        if st.button("➡️ Fase 4"):
            st.session_state.fase = 4
            st.session_state.validado = False
            st.session_state["fase3"] = ""
            st.rerun()

# =================================================
# FASE 4
# =================================================
elif st.session_state.fase == 4:

    st.header("🧬 Fase 4 — Reação Composta")

    st.markdown("""
    ### R(z) = cos(3z² + 2z)
    Calcule usando a regra da cadeia.
    """)

    z = sp.symbols('z')
    funcao = sp.cos(3*z**2 + 2*z)
    resposta_correta = sp.diff(funcao, z)

    resposta = st.text_input("Digite a taxa de variação:", key="fase4")

    if resposta and not st.session_state.validado:
        try:
            resp = converter_resposta(resposta)

            if sp.simplify(resp - resposta_correta) == 0:
                st.success("🧬 Reação estabilizada!")
                st.session_state.validado = True
            else:
                st.error("❌ Revise a regra da cadeia.")
        except:
            pass

    if st.session_state.validado:
        if st.button("➡️ Fase 5"):
            st.session_state.fase = 5
            st.session_state.validado = False
            st.session_state["fase4"] = ""
            st.rerun()

# =================================================
# FASE 5
# =================================================
elif st.session_state.fase == 5:

    st.header("🔥 Fase Final — O Sistema Supremo")

    st.markdown("""
    ### S(w) = [(w² + 1) · eʷ] / sin(w)
    Combine produto, quociente e cadeia.
    """)

    w = sp.symbols('w')
    funcao = ((w**2 + 1) * sp.exp(w)) / sp.sin(w)
    resposta_correta = sp.diff(funcao, w)

    resposta = st.text_input("Digite a taxa de variação final:", key="fase5")

    if resposta and not st.session_state.validado:
        try:
            resp = converter_resposta(resposta)

            if sp.simplify(resp - resposta_correta) == 0:
                st.success("🏆 MISSÃO COMPLETA!")
                st.balloons()
                st.session_state.validado = True
            else:
                st.error("❌ O sistema ainda não está estável.")
        except:
            pass
