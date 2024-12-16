import streamlit  as st
import  pandas as pd
from datetime import date

st.set_page_config(
    page_title="Cadastro de Cliente",
    page_icon="🖥"
)


def gravar_dados(nome,data_nascimento,tipo):
    if nome and data_nascimento <= date.today():
        with open("clientes.csv","a",encoding="utf-8") as file:
            file.write(f"{nome},{data_nascimento},{tipo}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False
        

st.title("Cadastro de Cliente")
st.divider()

nome = st.text_input("Digite o nome do cliente",
                     key="nome_cliente")

data_nascimento = st.date_input("Data Cadastro", format="DD/MM/YYYY")

tipo = st.selectbox("Tipo de Cliente",
                    ["Pessoa Jurídica", "Pessoa Física"])

btn_cadastrar =st.button("Cadastrar",
                         on_click= gravar_dados,
                         args=[nome,data_nascimento,tipo])

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!")                
    else:
        st.error("Houve algum problema no cadastro",
                 icon="❗")