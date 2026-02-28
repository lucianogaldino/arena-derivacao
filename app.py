import streamlit as st
import sympy as sp
import re

# -------------------------------------------------
# CONFIGURAÇÃO
# -------------------------------------------------
st.set_page_config(page_title="Guardiões da Taxa de Variação", page_icon="⚔️")
st.title("⚔️ Guardiões da Taxa de Variação — Nível Avançado")

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
# FASE 1 — DEFINIÇÃO (mais termos)
# =================================================
if st.session_state.fase == 1:

    st.header("🧪 Fase 1 — O Núcleo Fundamental")

    st.markdown("""
    O reator central agora possui múltiplos componentes energéticos.

    ### E(t) = t³ − 2t² + 5t − 7

    Para ativar o núcleo manualmente,  
    calcule a **taxa de variação usando a definição formal (limite do quociente incremental)**.
    """)

    t = sp.symbols('t')
    funcao = t**3 - 2*t**2 + 5*t - 7
    resposta_correta = sp.diff(funcao, t)

    resposta = st.text_input("Digite a taxa de variação:")

    if resposta:
        try:
            resp = sp.sympify(normalizar(resposta))
            if sp.simplify(resp - resposta_correta) == 0:
                st.success("🔥 Núcleo ativado com sucesso!")
                if st.button("➡️ Fase 2"):
                    st.session_state.fase = 2
            else:
                st.error("❌ Revise a aplicação da definição.")
        except:
            st.error("Formato inválido.")

# =================================================
# FASE 2 — PRODUTO (com trigonometria)
# =================================================
elif st.session_state.fase == 2:

    st.header("⚙️ Fase 2 — Engrenagens Trigonométricas")

    st.markdown("""
    O sistema mecânico agora envolve oscilação angular.

    ### F(x) = (x² + 1) · sin(x)

    Para estabilizar o sistema,  
    calcule a **taxa de variação usando a regra do produto**.
    """)

    x = sp.symbols('x')
    funcao = (x**2 + 1)*sp.sin(x)
    resposta_correta = sp.diff(funcao, x)

    resposta = st.text_input("Digite a taxa de variação:")

    if resposta:
        try:
            resp = sp.sympify(normalizar(resposta))
            if sp.simplify(resp - resposta_correta) == 0:
                st.success("⚙️ Engrenagens estabilizadas!")
                if st.button("➡️ Fase 3"):
                    st.session_state.fase = 3
            else:
                st.error("❌ Revise a regra do produto.")
        except:
            st.error("Formato inválido.")

# =================================================
# FASE 3 — QUOCIENTE (com exponencial)
# =================================================
elif st.session_state.fase == 3:

    st.header("🌊 Fase 3 — Fluxo Exponencial")

    st.markdown("""
    O fluxo energético cresce exponencialmente.

    ### Q(y) = eʸ / (y² + 1)

    Para manter o equilíbrio,  
    calcule a **taxa de variação usando a regra do quociente**.
    """)

    y = sp.symbols('y')
    funcao = sp.exp(y)/(y**2 + 1)
    resposta_correta = sp.diff(funcao, y)

    resposta = st.text_input("Digite a taxa de variação:")

    if resposta:
        try:
            resp = sp.sympify(normalizar(resposta))
            if sp.simplify(resp - resposta_correta) == 0:
                st.success("🌊 Fluxo controlado!")
                if st.button("➡️ Fase 4"):
                    st.session_state.fase = 4
            else:
                st.error("❌ Revise a regra do quociente.")
        except:
            st.error("Formato inválido.")

# =================================================
# FASE 4 — CADEIA (trig dentro)
# =================================================
elif st.session_state.fase == 4:

    st.header("🧬 Fase 4 — Reação Composta")

    st.markdown("""
    A reação química agora envolve composição trigonométrica.

    ### R(z) = cos(3z² + 2z)

    Calcule a **taxa de variação usando a regra da cadeia**.
    """)

    z = sp.symbols('z')
    funcao = sp.cos(3*z**2 + 2*z)
    resposta_correta = sp.diff(funcao, z)

    resposta = st.text_input("Digite a taxa de variação:")

    if resposta:
        try:
            resp = sp.sympify(normalizar(resposta))
            if sp.simplify(resp - resposta_correta) == 0:
                st.success("🧬 Reação estabilizada!")
                if st.button("➡️ Fase 5"):
                    st.session_state.fase = 5
            else:
                st.error("❌ Revise a regra da cadeia.")
        except:
            st.error("Formato inválido.")

# =================================================
# FASE 5 — COMBINAÇÃO (nível chefe)
# =================================================
elif st.session_state.fase == 5:

    st.header("🔥 Fase Final — O Sistema Supremo")

    st.markdown("""
    Agora todos os sistemas estão interligados:

    ### S(w) = [(w² + 1) · eʷ] / sin(w)

    Aqui você precisará combinar:
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
            resp = sp.sympify(normalizar(resposta))
            if sp.simplify(resp - resposta_correta) == 0:
                st.success("🏆 MISSÃO COMPLETA! Você domina cálculo avançado!")
                st.balloons()
            else:
                st.error("❌ O sistema ainda não está estável.")
        except:
            st.error("Formato inválido.")
