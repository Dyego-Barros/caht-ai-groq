import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os

load_dotenv()

def main():
    st.set_page_config(page_title="Chat com IA", layout="centered")
    st.title("🤖 Chat com IA")

    # Inicializa histórico
    if "historico" not in st.session_state:
        st.session_state.historico = []

    # Sidebar
    st.sidebar.title("Configurações")

    # Lista de modelos disponíveis
    modelos_disponiveis = [
        "gemma2-9b-it",
        "llama-3.1-8b-instant",
        "llama-3.1-8b-instant",
        "llama3-70b-8192",
        "llama3-8b-8192",
        "mistral-saba-24b"
    ]

    # Seleção do modelo e temperatura na sidebar
    modelo_selecionado = st.sidebar.selectbox("Selecione o modelo", modelos_disponiveis)
    temperatura = st.sidebar.slider("Temperatura", min_value=0.0, max_value=1.0, value=0.5, step=0.05)

    # Modelo com streaming
    llm = ChatGroq(
        api_key=os.environ.get("GROQ_API_KEY"),
        model=modelo_selecionado,
        temperature=temperatura,
        max_retries=2,
        streaming=True
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "Sua resposta sempre deverá ser em português brasileiro independente da língua usada na entrada."),
        ("human", "{pergunta}")
    ])

    # Mostra histórico anterior
    for pergunta, resposta in st.session_state.historico:
        with st.chat_message("user"):
            st.markdown(pergunta)
        with st.chat_message("assistant"):
            st.markdown(resposta)

    # Input padrão de chat que envia com Enter
    pergunta = st.chat_input("Digite sua pergunta e pressione Enter...")

    if pergunta:
        # Exibe a pergunta imediatamente
        with st.chat_message("user"):
            st.markdown(pergunta)

        # Streaming da resposta
        with st.chat_message("assistant"):
            resposta_container = st.empty()
            resposta_texto = ""
            mensagem = prompt.format_prompt(pergunta=pergunta).to_messages()

            for chunk in llm.stream(mensagem):
                if hasattr(chunk, "content") and chunk.content:
                    resposta_texto += chunk.content
                    resposta_container.markdown(resposta_texto + "▌")

            resposta_container.markdown(resposta_texto)

        # Salva no histórico
        st.session_state.historico.append((pergunta, resposta_texto))

if __name__ == "__main__":
    main()
