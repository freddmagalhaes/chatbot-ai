import time
import streamlit as st
from google import genai
from google.genai.errors import ServerError

from chat_layout import apply_stile_chat


st.set_page_config(page_title="Chatbot de IA", page_icon="🤖")
apply_stile_chat()


def inicializar_historico():
    if "historico" not in st.session_state:
        st.session_state.historico = []


def mostrar_historico():
    for role, msg in st.session_state.historico:
        if role == "user":
            with st.chat_message("user"):
                st.markdown(f"<div style='padding: 0.2rem 0.1rem;'>{msg}</div>", unsafe_allow_html=True)
        else:
            with st.chat_message("assistant"):
                st.markdown(msg)


def obter_chat():
    if "gemini_chat" not in st.session_state:
        try:
            api_key = st.secrets["GOOGLE_API_KEY"]
        except KeyError:
            raise ValueError(
                "A variável GOOGLE_API_KEY não foi encontrada nos Secrets do Streamlit."
            )

        client = genai.Client(api_key=api_key)

        st.session_state.gemini_client = client
        st.session_state.gemini_chat = client.chats.create(
            model="gemini-3.8-flash"
        )

    return st.session_state.gemini_chat


def responder_gemini(chat, prompt: str) -> str:
    max_tentativas = 5

    for tentativa in range(max_tentativas):
        try:
            resposta = chat.send_message(prompt)
            return resposta.text

        except ServerError:
            if tentativa == max_tentativas - 1:
                raise RuntimeError(
                    "O servidor do Gemini está temporariamente indisponível. "
                    "Tente novamente em alguns instantes."
                )
            time.sleep(2 ** tentativa)

        except Exception as e:
            raise RuntimeError(f"Erro ao consultar o Gemini: {e}")

    raise RuntimeError("Não foi possível obter resposta do Gemini.")


st.title("Chatbot de IA")

inicializar_historico()

if "mensagem_inicial" not in st.session_state:
    st.session_state.mensagem_inicial = True

if st.session_state.mensagem_inicial:
    st.info("Olá! Me pergunte algo e eu vou responder usando o Gemini.")
    st.session_state.mensagem_inicial = False

mostrar_historico()

st.sidebar.title("Menu")
if st.sidebar.button("Nova conversa", use_container_width=True):
    st.session_state.historico = []
    if "gemini_chat" in st.session_state:
        del st.session_state.gemini_chat
    if "gemini_client" in st.session_state:
        del st.session_state.gemini_client
    st.session_state.mensagem_inicial = True
    st.rerun()

prompt = st.chat_input("Digite sua mensagem:")

if prompt:
    st.chat_message("user").markdown(f"<div style='padding: 0.2rem 0.1rem;'>{prompt}</div>", unsafe_allow_html=True)
    st.session_state.historico.append(("user", prompt))

    try:
        chat = obter_chat()
        resposta = responder_gemini(chat, prompt)
    except Exception as e:
        st.error(str(e))
        st.stop()

    with st.chat_message("assistant"):
        st.markdown(resposta)

    st.session_state.historico.append(("assistant", resposta))
