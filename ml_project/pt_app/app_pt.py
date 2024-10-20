import streamlit as st
import pandas as pd
from sklearn import linear_model


if __name__ == '__main__':
    st.set_page_config(
    page_title="Previsão - Preço da pizza",  # Título da aba do navegador
    page_icon="🍕",  # Ícone da aba do navegador
    layout="centered",  # Define o layout da página (wide ou centered)
    )
    df = pd.read_csv('./pt_app/pizzas.csv')

    modelo =  linear_model.LinearRegression()

    #### dados de treino
    x = df[["diametro"]]
    y = df[["preco"]]

    ##### treino
    modelo.fit(x,y)

    img_url = "https://i.pinimg.com/enabled/564x/ff/c3/f4/ffc3f4a4862f12efccc593df457e2234.jpg"
    # st.markdown(
    #     """
    #     <style>
    #     body {
    #         background-color: #ff0000;  /* Mudar a cor de fundo */
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )
    # st.title()
    st.markdown(
        f"""
        <div style="text-align: center; font-size: 40px;">
            Prevendo o valor da pizza
        </div>
        """, unsafe_allow_html=True
    )
    diametro = st.number_input("Digite o tamanho do diametro desejado para obter o preço da pizza")
    if diametro:
        preco_previsto = modelo.predict([[diametro]])
        result = f'Para pizza de {int(diametro)} diametro o valor é de R$ {round(float(preco_previsto[0][0]),2)} reais!'
        st.markdown(
        f"""
        <div style="text-align: center; font-size: 24px;">
            {result}<br>
        </div>
        """, 
        unsafe_allow_html=True
        )


    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <img src="{img_url}" alt="Minha Imagem" style="width:40%;">
        </div>
        <div style="text-align: center; font-size: 24px;">
            @ clar - 2024 <br>
        </div>
        """, unsafe_allow_html=True
    )


    st.divider()
