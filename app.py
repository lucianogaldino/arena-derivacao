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

# =================================================
# SESSION STATE
# =================================================
if "fase" not in st.session_state:
    st.session_state.fase = 1

if "validado" not in st.session_state:
    st.session_state.validado = False

if "pontos" not in st.session_state:
    st.session_state.pontos = 100  # começa com 100 pontos

# =================================================
# SIDEBAR
# =================================================
st.sidebar.title("📊 Progresso")
st.sidebar.progress(st.session_state.fase / 5)
st.sidebar.write(f"Fase {st.session_state.fase} de 5")

st.sidebar.markdown("---")
st.sidebar.subheader("🏆 Pontuação")
st.sidebar.write(f"**{st.session_state.pontos} pontos**")

if st.button("🔄 Reiniciar Missão"):

    st.session_state.fase = 1
    st.session_state.pontos = 100
    st.session_state.validado = False

    # RESET DA FASE FINAL
    st.session_state.pontuacao_final_calculada = False

    # Limpar inputs
    for chave in list(st.session_state.keys()):
        if "input" in chave:
            del st.session_state[chave]

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
            st.session_state.pontos -= 10  # perde 10 por erro
    except:
        st.error("⚠️ Expressão inválida.")
        st.session_state.pontos -= 10  # também perde se expressão for inválida

# =================================================
# MODELO DE FASE (mantido igual, só adicionando bônus)
# =================================================

def avancar_fase(proxima):
    st.session_state.fase = proxima
    st.session_state.validado = False
    st.session_state.pontos += 100  # ganha 100 ao avançar
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

Seu objetivo: determinar como essa energia varia instantaneamente, indicando a taxa de variação para estabilizar o núcleo e desbloquear o próximo setor.

E(t) = t³ − 2t² + 5t − 7
""")

    resposta = st.text_input("Digite a solução encontrada:", key="f1_input")
    confirmar = st.button("⚔️ Estabilizar Núcleo", key="f1_btn")

    if confirmar and not st.session_state.validado:
        validar_resposta(resposta, resposta_correta, "🔥 Núcleo ativado com sucesso!")

    if st.session_state.validado:
        if st.button("➡️ Fase 2"):
            avancar_fase(2)

# =================================================
# FASE 2
# =================================================
elif st.session_state.fase == 2:

    st.header("⚙️ Fase 2 — Engrenagens Trigonométricas")

    x = sp.symbols('x')
    funcao = (x**2 + 1) * sp.sin(x)
    resposta_correta = sp.diff(funcao, x)

    st.markdown("""
⚙️ No setor de acionamentos mecânicos as engrenagens começaram a oscilar. 
O movimento depende de dois sistemas interligados e obedece a função abaixo.

Para restaurar o equilíbrio e reativar as engrenagens, é necessário descobrir como essa grandeza varia no instante atual.

F(x) = (x² + 1) · sin(x)
""")

    resposta = st.text_input("Digite a solução encontrada:", key="f2_input")
    confirmar = st.button("⚙️ Regular Oscilação", key="f2_btn")

    if confirmar and not st.session_state.validado:
        validar_resposta(resposta, resposta_correta, "⚙️ Engrenagens estabilizadas!")

    if st.session_state.validado:
        if st.button("➡️ Fase 3"):
            avancar_fase(3)

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

Ele cresce rapidamente, obedecendo a função abaixo, e se não for controlado pode causar sobrecarga.

Determine como essa intensidade varia para controlar a emissão desse fluxo.

Q(y) = eʸ / (y² + 1)
""")

    resposta = st.text_input("Digite a solução encontrada:", key="f3_input")
    confirmar = st.button("🌊 Controlar Fluxo", key="f3_btn")

    if confirmar and not st.session_state.validado:
        validar_resposta(resposta, resposta_correta, "🌊 Fluxo controlado!")

    if st.session_state.validado:
        if st.button("➡️ Fase 4"):
            avancar_fase(4)

# =================================================
# FASE 4
# =================================================
elif st.session_state.fase == 4:

    st.header("🧬 Fase 4 — Reação Composta")

    z = sp.symbols('z')
    funcao = sp.cos(3*z**2 + 2*z)
    resposta_correta = sp.diff(funcao, z)

    st.markdown("""
🧬 No sistema secundário está ocorrendo um processo de transformação química.

A reação depende de uma composição interna complexa.

Analise como essa função varia e estabilize a reação.

R(z) = cos(3z² + 2z)
""")

    resposta = st.text_input("Digite a solução encontrada:", key="f4_input")
    confirmar = st.button("🧬 Estabilizar Reação", key="f4_btn")

    if confirmar and not st.session_state.validado:
        validar_resposta(resposta, resposta_correta, "🧬 Reação estabilizada!")

    if st.session_state.validado:
        if st.button("➡️ Fase 5"):
            avancar_fase(5)

# =================================================
# FASE 5
# =================================================
elif st.session_state.fase == 5:

    if "pontuacao_final_calculada" not in st.session_state:
        st.session_state.pontuacao_final_calculada = False

    st.header("🔥 Fase Final — O Sistema Supremo")

    w = sp.symbols('w')
    funcao = ((w**2 + 1) * sp.exp(w)) / sp.sin(w)
    resposta_correta = sp.diff(funcao, w)

    st.markdown("""
🔥 SISTEMA SUPREMO ATIVADO

Todos os módulos estão conectados. Isso é sinal de catástrofe!

Agora você precisa calcular como o sistema completo varia para impedir o colapso total.

S(w) = [(w² + 1) · eʷ] / sin(w)

Boa sorte!!!
""")

    resposta = st.text_input(
        "Digite a solução encontrada:",
        key="f5_input",
        disabled=st.session_state.validado
    )

    confirmar = st.button(
        "🔥 Impedir Colapso",
        key="f5_btn",
        disabled=st.session_state.validado
    )

    # Validação normal
    if confirmar and not st.session_state.validado:
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

    # Se já calculou, apenas mostra resultado
    if st.session_state.pontuacao_final_calculada:
        st.success(f"🎯 Pontuação Final: {st.session_state.pontos} pontos!")
