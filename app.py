import streamlit as st
import sympy as sp
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application
)

# =================================================
# CONFIGURAÇÃO DO PARSER
# =================================================
transformations = standard_transformations + (implicit_multiplication_application,)

def converter_resposta(resposta):
    resposta = resposta.replace("^", "**")
    return parse_expr(
        resposta,
        transformations=transformations,
        local_dict={"e": sp.E}
    )

# =================================================
# CONFIGURAÇÃO GERAL
# =================================================
st.set_page_config(page_title="Guardiões da Taxa de Variação", page_icon="⚔️")
st.title("⚔️ Guardiões da Taxa de Variação — Nível Avançado")

st.markdown("""
Calcule a **derivada** da função apresentada.

Use:
- Multiplicação → `*`
- Potência → `**`
- Divisão → `/`
- Trigonométricas → `sin(x)`, `cos(x)`
- Exponencial → `e`
""")

# =================================================
# SESSION STATE
# =================================================
if "fase" not in st.session_state:
    st.session_state.fase = 1

if "validado" not in st.session_state:
    st.session_state.validado = False

# =================================================
# SIDEBAR
# =================================================
st.sidebar.title("📊 Progresso")
st.sidebar.progress(st.session_state.fase / 5)
st.sidebar.write(f"Fase {st.session_state.fase} de 5")

if st.sidebar.button("🔄 Reiniciar Missão"):
    st.session_state.fase = 1
    st.session_state.validado = False
    st.rerun()

# =================================================
# FUNÇÃO DE VALIDAÇÃO
# =================================================
def validar_resposta(resposta, resposta_correta, mensagem_sucesso):
    try:
        resp = converter_resposta(resposta)
        if sp.simplify(resp - resposta_correta) == 0:
            st.success(mensagem_sucesso)
            st.session_state.validado = True
        else:
            st.error("❌ Resposta incorreta.")
    except:
        st.error("⚠️ Expressão inválida.")

# =================================================
# FASE 1
# =================================================
if st.session_state.fase == 1:

    st.header("🧪 Fase 1 — O Núcleo Fundamental")

    t = sp.symbols('t')
    funcao = t**3 - 2*t**2 + 5*t - 7
    resposta_correta = sp.diff(funcao, t)

    st.write("E(t) = t³ − 2t² + 5t − 7")

    resposta = st.text_input("Digite a solução encontrada:", key="f1_input")
    confirmar = st.button("⚔️ Confirmar Resposta", key="f1_btn")

    if confirmar and not st.session_state.validado:
        validar_resposta(resposta, resposta_correta, "🔥 Núcleo ativado com sucesso!")

    if st.session_state.validado:
        if st.button("➡️ Fase 2"):
            st.session_state.fase = 2
            st.session_state.validado = False
            st.rerun()

# =================================================
# FASE 2
# =================================================
elif st.session_state.fase == 2:

    st.header("⚙️ Fase 2 — Engrenagens Trigonométricas")

    x = sp.symbols('x')
    funcao = (x**2 + 1) * sp.sin(x)
    resposta_correta = sp.diff(funcao, x)

    st.write("F(x) = (x² + 1)·sin(x)")

    resposta = st.text_input("Digite a solução encontrada:", key="f2_input")
    confirmar = st.button("⚙️ Confirmar Resposta", key="f2_btn")

    if confirmar and not st.session_state.validado:
        validar_resposta(resposta, resposta_correta, "⚙️ Engrenagens estabilizadas!")

    if st.session_state.validado:
        if st.button("➡️ Fase 3"):
            st.session_state.fase = 3
            st.session_state.validado = False
            st.rerun()

# =================================================
# FASE 3
# =================================================
elif st.session_state.fase == 3:

    st.header("🌊 Fase 3 — Fluxo Exponencial")

    y = sp.symbols('y')
    funcao = sp.exp(y) / (y**2 + 1)
    resposta_correta = sp.diff(funcao, y)

    st.write("Q(y) = eʸ / (y² + 1)")

    resposta = st.text_input("Digite a solução encontrada:", key="f3_input")
    confirmar = st.button("🌊 Confirmar Resposta", key="f3_btn")

    if confirmar and not st.session_state.validado:
        validar_resposta(resposta, resposta_correta, "🌊 Fluxo controlado!")

    if st.session_state.validado:
        if st.button("➡️ Fase 4"):
            st.session_state.fase = 4
            st.session_state.validado = False
            st.rerun()

# =================================================
# FASE 4
# =================================================
elif st.session_state.fase == 4:

    st.header("🧬 Fase 4 — Reação Composta")

    z = sp.symbols('z')
    funcao = sp.cos(3*z**2 + 2*z)
    resposta_correta = sp.diff(funcao, z)

    st.write("R(z) = cos(3z² + 2z)")

    resposta = st.text_input("Digite a solução encontrada:", key="f4_input")
    confirmar = st.button("🧬 Confirmar Resposta", key="f4_btn")

    if confirmar and not st.session_state.validado:
        validar_resposta(resposta, resposta_correta, "🧬 Reação estabilizada!")

    if st.session_state.validado:
        if st.button("➡️ Fase 5"):
            st.session_state.fase = 5
            st.session_state.validado = False
            st.rerun()

# =================================================
# FASE 5
# =================================================
elif st.session_state.fase == 5:

    st.header("🔥 Fase Final — O Sistema Supremo")

    w = sp.symbols('w')
    funcao = ((w**2 + 1) * sp.exp(w)) / sp.sin(w)
    resposta_correta = sp.diff(funcao, w)

    st.write("S(w) = [(w² + 1)·eʷ] / sin(w)")

    resposta = st.text_input("Digite a solução encontrada:", key="f5_input")
    confirmar = st.button("🔥 Confirmar Resposta", key="f5_btn")

    if confirmar and not st.session_state.validado:
        validar_resposta(resposta, resposta_correta, "🏆 MISSÃO COMPLETA!")

        if st.session_state.validado:
            st.balloons()
