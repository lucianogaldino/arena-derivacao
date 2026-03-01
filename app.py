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
# 🌌 Bem-vindo ao Laboratório da Taxa de Variação

Um sistema energético avançado entrou em colapso...

Para estabilizar cada núcleo, você precisará calcular a **taxa de variação** das funções apresentadas.

⚙️ Para escrever as expressões use:

- Multiplicação → `*`
- Potência → `**`
- Divisão → `/`
- Funções trigonométricas → `sin(x)`, `cos(x)`
- Exponencial → `e` (representa a constante de Euler)

💡 Digite sua resposta em formato matemático e avance pelas fases.
""")

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
# FASE 1
# =================================================
if st.session_state.fase == 1:

    st.header("🧪 Fase 1 — O Núcleo Fundamental")

    t = sp.symbols('t')
    funcao = t**3 - 2*t**2 + 5*t - 7
    resposta_correta = sp.diff(funcao, t)

    st.markdown("""
🛰 Um núcleo primário está instável.

A energia armazenada depende do tempo, conforme função abaixo, e está crescendo perigosamente.

Seu objetivo: determinar como essa energia varia instantaneamente, calculando a taxa de variação para estabilizar o núcleo e desbloquear o próximo setor.

E(t) = t³ − 2t² + 5t − 7
    """)

    resposta = st.text_input(
        "Digite a taxa de variação:",
        key=f"fase1_{st.session_state.fase}"
    )

    if resposta and not st.session_state.validado:
        try:
            resp = converter_resposta(resposta)

            if sp.simplify(resp - resposta_correta) == 0:
                st.success("🔥 Núcleo ativado com sucesso!")
                st.session_state.validado = True
            else:
                st.error("❌ Resposta incorreta.")
        except:
            pass

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

    st.markdown("""
⚙️ Engrenagens mecânicas começaram a oscilar.

O movimento depende de dois sistemas interligados e obedece a função abaixo.

Para restaurar o equilíbrio e reativar as engrenagens, descubra como essa grandeza varia no instante atual.

F(x) = (x² + 1) · sin(x)    """)

    resposta = st.text_input(
        "Digite a taxa de variação:",
        key=f"fase2_{st.session_state.fase}"
    )

    if resposta and not st.session_state.validado:
        try:
            resp = converter_resposta(resposta)

            if sp.simplify(resp - resposta_correta) == 0:
                st.success("⚙️ Engrenagens estabilizadas!")
                st.session_state.validado = True
            else:
                st.error("❌ Resposta incorreta.")
        except:
            pass

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

    st.markdown("""
🌊 Um fluxo energético atravessa o sistema central.

Ele cresce rapidamente, obedecendo a função abaixo, e pode causar sobrecarga.

Determine a função que determina como essa intensidade varia para controlar o fluxo e avançar.

Q(y) = eʸ / (y² + 1)    """)

    resposta = st.text_input(
        "Digite a taxa de variação:",
        key=f"fase3_{st.session_state.fase}"
    )

    if resposta and not st.session_state.validado:
        try:
            resp = converter_resposta(resposta)

            if sp.simplify(resp - resposta_correta) == 0:
                st.success("🌊 Fluxo controlado!")
                st.session_state.validado = True
            else:
                st.error("❌ Resposta incorreta.")
        except:
            pass

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

    st.markdown("""
🧬 Um processo de transformação química está ocorrendo.

A reação depende de uma composição interna complexa, conforme função abaixo.

Analise como essa função varia e estabilize a reação.

R(z) = cos(3z² + 2z) """)

    resposta = st.text_input(
        "Digite a taxa de variação:",
        key=f"fase4_{st.session_state.fase}"
    )

    if resposta and not st.session_state.validado:
        try:
            resp = converter_resposta(resposta)

            if sp.simplify(resp - resposta_correta) == 0:
                st.success("🧬 Reação estabilizada!")
                st.session_state.validado = True
            else:
                st.error("❌ Resposta incorreta.")
        except:
            pass

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

    st.markdown("""
🔥 SISTEMA SUPREMO ATIVADO

Todos os módulos estão conectados.

Agora você precisa calcular como o sistema completo, dado pela função abaixo, varia para impedir o colapso total.

Se conseguir, a missão será concluída!!!Boa Sorte!!!

S(w) = [(w² + 1) · eʷ] / sin(w)    """)

    resposta = st.text_input(
        "Digite a taxa de variação final:",
        key=f"fase5_{st.session_state.fase}"
    )

    if resposta and not st.session_state.validado:
        try:
            resp = converter_resposta(resposta)

            if sp.simplify(resp - resposta_correta) == 0:
                st.success("🏆 MISSÃO COMPLETA!")
                st.balloons()
                st.session_state.validado = True
            else:
                st.error("❌ Resposta incorreta.")
        except:
            pass
