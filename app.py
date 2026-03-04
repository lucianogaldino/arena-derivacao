import streamlit as st
import sympy as sp

st.set_page_config(page_title="Missão Derivadas", page_icon="🚀")

# ==========================================================
# INICIALIZAÇÃO DO ESTADO
# ==========================================================
if "fase" not in st.session_state:
    st.session_state.fase = 1

if "pontos" not in st.session_state:
    st.session_state.pontos = 100

if "validado" not in st.session_state:
    st.session_state.validado = False

if "pontuacao_final_calculada" not in st.session_state:
    st.session_state.pontuacao_final_calculada = False


# ==========================================================
# FUNÇÃO CONVERSÃO
# ==========================================================
def converter_resposta(expr):
    return sp.sympify(expr.replace("^", "**"))


# ==========================================================
# TOPO
# ==========================================================
st.title("🚀 Missão: Salvar o Sistema das Derivadas")

st.markdown(f"### 🎯 Pontuação Atual: {st.session_state.pontos} pontos")
st.markdown("---")


# ==========================================================
# FASE 1
# ==========================================================
if st.session_state.fase == 1:

    st.header("🟢 Fase 1 — Sistema Linear Inicial")

    x = sp.symbols("x")
    resposta_correta = sp.diff(3*x**2 + 2*x, x)

    st.markdown("""
O sistema principal foi iniciado.

Você precisa calcular a taxa de variação da função:

f(x) = 3x² + 2x
""")

    resposta = st.text_input("Digite a derivada:", key="f1_input")

    if st.button("Confirmar", key="f1_btn"):

        try:
            resp = converter_resposta(resposta)

            if sp.simplify(resp - resposta_correta) == 0:
                st.success("✅ Correto! Avançando de fase.")
                st.session_state.pontos += 100
                st.session_state.fase = 2
                st.rerun()
            else:
                st.error("❌ Incorreto.")
                st.session_state.pontos -= 10

        except:
            st.error("⚠️ Expressão inválida.")
            st.session_state.pontos -= 10


# ==========================================================
# FASE 2
# ==========================================================
elif st.session_state.fase == 2:

    st.header("🟡 Fase 2 — Regra do Produto")

    x = sp.symbols("x")
    resposta_correta = sp.diff(x**2 * sp.sin(x), x)

    st.markdown("""
O sistema está instável.

Calcule a derivada:

f(x) = x² · sen(x)
""")

    resposta = st.text_input("Digite a derivada:", key="f2_input")

    if st.button("Confirmar", key="f2_btn"):

        try:
            resp = converter_resposta(resposta)

            if sp.simplify(resp - resposta_correta) == 0:
                st.success("✅ Correto! Avançando.")
                st.session_state.pontos += 100
                st.session_state.fase = 3
                st.rerun()
            else:
                st.error("❌ Incorreto.")
                st.session_state.pontos -= 10

        except:
            st.error("⚠️ Expressão inválida.")
            st.session_state.pontos -= 10


# ==========================================================
# FASE 3
# ==========================================================
elif st.session_state.fase == 3:

    st.header("🟠 Fase 3 — Regra do Quociente")

    x = sp.symbols("x")
    resposta_correta = sp.diff((x**2 + 1) / x, x)

    st.markdown("""
Novo desafio detectado.

Calcule:

f(x) = (x² + 1) / x
""")

    resposta = st.text_input("Digite a derivada:", key="f3_input")

    if st.button("Confirmar", key="f3_btn"):

        try:
            resp = converter_resposta(resposta)

            if sp.simplify(resp - resposta_correta) == 0:
                st.success("✅ Excelente! Avançando.")
                st.session_state.pontos += 100
                st.session_state.fase = 4
                st.rerun()
            else:
                st.error("❌ Incorreto.")
                st.session_state.pontos -= 10

        except:
            st.error("⚠️ Expressão inválida.")
            st.session_state.pontos -= 10


# ==========================================================
# FASE 4
# ==========================================================
elif st.session_state.fase == 4:

    st.header("🔴 Fase 4 — Regra da Cadeia")

    x = sp.symbols("x")
    resposta_correta = sp.diff(sp.sin(x**2), x)

    st.markdown("""
Sistema quase colapsando!

Calcule:

f(x) = sen(x²)
""")

    resposta = st.text_input("Digite a derivada:", key="f4_input")

    if st.button("Confirmar", key="f4_btn"):

        try:
            resp = converter_resposta(resposta)

            if sp.simplify(resp - resposta_correta) == 0:
                st.success("🔥 Última fase desbloqueada!")
                st.session_state.pontos += 100
                st.session_state.fase = 5
                st.rerun()
            else:
                st.error("❌ Incorreto.")
                st.session_state.pontos -= 10

        except:
            st.error("⚠️ Expressão inválida.")
            st.session_state.pontos -= 10


# ==========================================================
# FASE 5
# ==========================================================
elif st.session_state.fase == 5:

    st.header("🔥 Fase Final — Sistema Supremo")

    w = sp.symbols("w")
    funcao = ((w**2 + 1) * sp.exp(w)) / sp.sin(w)
    resposta_correta = sp.diff(funcao, w)

    st.markdown("""
🔥 SISTEMA SUPREMO ATIVADO

Calcule:

S(w) = [(w² + 1) · eʷ] / sen(w)
""")

    resposta = st.text_input(
        "Digite a solução encontrada:",
        key="f5_input",
        disabled=st.session_state.validado
    )

    if st.button(
        "🔥 Impedir Colapso",
        key="f5_btn",
        disabled=st.session_state.validado
    ):

        try:
            resp = converter_resposta(resposta)

            if sp.simplify(resp - resposta_correta) == 0:
                st.session_state.validado = True
                st.success("🏆 MISSÃO COMPLETA!")
                st.balloons()
            else:
                st.error("❌ Resposta incorreta.")
                st.session_state.pontos -= 10

        except:
            st.error("⚠️ Expressão inválida.")
            st.session_state.pontos -= 10

    # Botão separado para pontuação final
    if st.session_state.validado and not st.session_state.pontuacao_final_calculada:

        if st.button("🏆 Clique para calcular pontuação final"):
            st.session_state.pontos *= 2
            st.session_state.pontuacao_final_calculada = True
            st.success(f"🎯 Pontuação Final: {st.session_state.pontos} pontos!")

    if st.session_state.pontuacao_final_calculada:
        st.success(f"🎯 Pontuação Final: {st.session_state.pontos} pontos!")


# ==========================================================
# BOTÃO GLOBAL DE REINICIAR
# ==========================================================
st.markdown("---")

if st.button("🔄 Reiniciar Missão"):

    st.session_state.fase = 1
    st.session_state.pontos = 100
    st.session_state.validado = False
    st.session_state.pontuacao_final_calculada = False

    for chave in list(st.session_state.keys()):
        if "input" in chave:
            del st.session_state[chave]

    st.rerun()
