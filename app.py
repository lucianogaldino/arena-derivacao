import streamlit as st
import sympy as sp

x = sp.symbols('x')

st.title("🎮 A Arena dos Códigos")

# Estado inicial
if "fase" not in st.session_state:
    st.session_state.fase = 1
    st.session_state.pontos = 0

# Estrutura das fases
fases = {
    1: {
        "funcao": 6*x**4 - 3*x**2 + 8*x - 5,
        "pontos": 100,
        "historia": "O módulo inicial controla o crescimento básico do personagem. O sistema precisa atualizar automaticamente a taxa de evolução."
    },
    2: {
        "funcao": x**3*(2*x-5),
        "pontos": 200,
        "historia": "O motor de ataque combina potência acumulada e intensidade momentânea. O algoritmo precisa recalcular essa combinação."
    },
    3: {
        "funcao": (x**2 + 4)/(x-1),
        "pontos": 300,
        "historia": "O escudo do personagem depende da razão entre energia e resistência estrutural. O sistema precisa recalibrar essa relação."
    },
    4: {
        "funcao": (4*x**2 - 3*x + 1)**5,
        "pontos": 400,
        "historia": "Ao atravessar o portal dimensional, o poder sofre uma transformação interna antes de ser amplificado."
    },
    5: {
        "funcao": (x**2*(2*x+3)**4)/(3*x-2),
        "pontos": 1000,
        "historia": "👑 O Algoritmo Supremo combina múltiplos sistemas internos. Apenas um código perfeitamente estruturado pode derrotá-lo."
    }
}

# Se ainda há fases
if st.session_state.fase <= 5:
    fase_atual = fases[st.session_state.fase]
    
    st.subheader(f"🔥 Fase {st.session_state.fase}")
    st.info(fase_atual["historia"])
    
    st.write("Derive a função:")
    st.latex(sp.latex(fase_atual["funcao"]))
    
    resposta = st.text_input("Digite sua derivada:")
    
    if st.button("Enviar"):
        try:
            resposta_usuario = sp.sympify(resposta)
            derivada_correta = sp.diff(fase_atual["funcao"], x)
            
            if sp.simplify(resposta_usuario - derivada_correta) == 0:
                st.success("✅ Código aceito! Próxima fase desbloqueada!")
                st.session_state.pontos += fase_atual["pontos"]
                st.session_state.fase += 1
                st.rerun()  # <-- faz avançar automaticamente
            else:
                st.error("❌ O núcleo rejeitou seu código. Tente novamente.")
        except:
            st.warning("⚠️ Erro na expressão digitada.")
    
    st.write("🏆 Pontuação:", st.session_state.pontos)

else:
    st.success("👑 VOCÊ DERROTOU O ALGORITMO SUPREMO!")
    st.write("Pontuação final:", st.session_state.pontos)
