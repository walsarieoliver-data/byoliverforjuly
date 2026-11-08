
import streamlit as st

st.set_page_config(
    page_title="Segredo do Oliver",
    page_icon="🤫"
)

st.title("🤫 Um segredo para Júlia")
st.write("Tenho uma coisa para te contar...")

if "etapa" not in st.session_state:
    st.session_state.etapa = "inicio"
    st.session_state.caminho = ""
    st.session_state.mensagens = [
        ("assistant", "Oi Júlia, tudo bem?")
    ]

for autor, mensagem in st.session_state.mensagens:
    with st.chat_message(autor):
        st.write(mensagem)

if st.session_state.etapa == "inicio":

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Sim ❤️", use_container_width=True):
            st.session_state.mensagens.append(("user", "Sim!"))
            st.session_state.mensagens.append(
                ("assistant",
                 "Que bom! Venho aqui te contar um segredo "
                 "sobre o Oliver, você quer saber?")
            )
            st.session_state.caminho = "sim"
            st.session_state.etapa = "segredo"
            st.rerun()

    with col2:
        if st.button("Não 😢", use_container_width=True):
            st.session_state.mensagens.append(("user", "Não."))
            st.session_state.mensagens.append(
                ("assistant",
                 "Que pena! Sabe uma coisa que pode te animar? "
                 "Um segredo sobre o Oliver, você quer saber?")
            )
            st.session_state.caminho = "nao"
            st.session_state.etapa = "segredo"
            st.rerun()

elif st.session_state.etapa == "segredo":

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Quero saber! ❤️", use_container_width=True):
            st.session_state.mensagens.append(
                ("user", "Sim! Quero saber!")
            )
            st.session_state.mensagens.append(
                ("assistant",
                 "Ele te acha linda e está louco pra te ver, "
                 "mas é segredo, tá? 🤫❤️")
            )
            st.session_state.etapa = "fim"
            st.rerun()

    with col2:
        if st.button("Não quero saber", use_container_width=True):
            st.session_state.mensagens.append(
                ("user", "Não quero saber.")
            )

            if st.session_state.caminho == "sim":
                resposta = "Okay, vamos fingir que eu não ia dizer nada."
            else:
                resposta = "Tá bom, finja que nunca tivemos essa conversa."

            st.session_state.mensagens.append(
                ("assistant", resposta)
            )
            st.session_state.etapa = "fim"
            st.rerun()

elif st.session_state.etapa == "fim":

    st.success("Fim da conversa! ❤️")

    if st.button("Conversar novamente 🔄"):
        st.session_state.clear()
        st.rerun()
