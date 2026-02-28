import streamlit as st
import sympy as sp
import re

# -------------------------------------------------
# CONFIGURAÇÃO
# -------------------------------------------------
st.set_page_config(page_title="Guardiões da Taxa de Variação", page_icon="⚔️")
st.title("⚔️ Guardiões da Taxa de Variação")

if "fase" not in st.session_state:
    st.session_state.fase = 1

# -------------------------------------------------
# NORMALIZAÇÃO
# -------------------------------------------------
def normalizar(expr):
    expr = expr.replace("^", "**")
    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)
    expr = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', expr)
    return expr

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
    O reator central de Chronópolis precisa de calibração manual.

    A energia é descrita por:

    ### E(t) = t² + 3t

    ⚠️ Para ativar o núcleo, você deve calcular a  
    **taxa de variação usando a definição formal (limite do quociente incremental)**.

    Determine a taxa de variação final simplificada.
    """)

    t = sp.symbols('t')
    funcao = t**2 + 3*t
    resposta_correta = sp.diff(funcao, t)

    resposta = st.text_input("Digite a taxa de variação:")

    if resposta:
        try:
            resp = sp.sympify(normalizar(resposta))
            if sp.simplify(resp - resposta_correta) == 0:
                st.success("🔥 Núcleo ativado por definição!")
                if st.button("➡️ Fase 2"):
                    st.session_state.fase = 2
            else:
                st.error("⚠️ A definição não foi aplicada corretamente.")
        except:
            st.error("Formato inválido.")

# =================================================
# FASE 2 — PRODUTO
# =================================================
elif st.session_state.fase == 2:

    st.header("⚙️ Fase 2 — Engrenagens Sincronizadas")

    st.markdown("""
    O sistema mecânico depende de duas forças multiplicadas:

    ### F(x) = (x² + 1)(3x)

    Para manter as engrenagens funcionando,  
    calcule a **taxa de variação usando a regra do produto**.
    """)

    x = sp.symbols('x')
    funcao = (x**2 + 1)*(3*x)
    resposta_correta = sp.diff(funcao, x)

    resposta = st.text_input("Digite a taxa de variação:")

    if resposta:
        try:
            resp = sp.sympify(normalizar(resposta))
            if sp.simplify(resp - resposta_correta) == 0:
                st.success("⚙️ Engrenagens sincronizadas!")
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

    st.header("🌊 Fase 3 — Fluxo Dividido")

    st.markdown("""
    O fluxo de energia agora é dado por:

    ### Q(y) = (2y³ + 1) / (y)

    Para equilibrar o sistema hidráulico,  
    determine a **taxa de variação usando a regra do quociente**.
    """)

    y = sp.symbols('y')
    funcao = (2*y**3 + 1)/y
    resposta_correta = sp.diff(funcao, y)

    resposta = st.text_input("Digite a taxa de variação:")

    if resposta:
        try:
            resp = sp.sympify(normalizar(resposta))
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

    st.header("🧬 Fase 4 — Reação em Cadeia")

    st.markdown("""
    A reação química depende de uma função dentro de outra:

    ### R(z) = (4z² + 1)³

    Para controlar a reação,  
    calcule a **taxa de variação usando a regra da cadeia**.
    """)

    z = sp.symbols('z')
    funcao = (4*z**2 + 1)**3
    resposta_correta = sp.diff(funcao, z)

    resposta = st.text_input("Digite a taxa de variação:")

    if resposta:
        try:
            resp = sp.sympify(normalizar(resposta))
            if sp.simplify(resp - resposta_correta) == 0:
                st.success("🧬 Reação controlada!")
                if st.button("➡️ Fase 5"):
                    st.session_state.fase = 5
            else:
                st.error("❌ Revise a regra da cadeia.")
        except:
            st.error("Formato inválido.")

# =================================================
# FASE 5 — COMBINAÇÃO
# =================================================
elif st.session_state.fase == 5:

    st.header("🔥 Fase Final — O Sistema Supremo")

    st.markdown("""
    Agora todos os sistemas estão interligados:

    ### S(w) = [(w² + 1)(2w)] / (w³)

    Você precisará combinar regras  
    (produto + quociente + simplificação).

    Calcule a **taxa de variação completa**.
    """)

    w = sp.symbols('w')
    funcao = ((w**2 + 1)*(2*w))/(w**3)
    resposta_correta = sp.diff(funcao, w)

    resposta = st.text_input("Digite a taxa de variação final:")

    if resposta:
        try:
            resp = sp.sympify(normalizar(resposta))
            if sp.simplify(resp - resposta_correta) == 0:
                st.success("🏆 MISSÃO COMPLETA! Você domina todas as regras!")
                st.balloons()
            else:
                st.error("❌ O sistema supremo ainda não está estável.")
        except:
            st.error("Formato inválido.")
