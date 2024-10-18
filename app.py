import streamlit as st
import pandas as pd
from sklearn import linear_model

df = pd.read_csv('pizzas.csv')

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
        Predicting pizza price by diameter
    </div>
    """, unsafe_allow_html=True
)
diametro = st.number_input("Enter the desired diameter size to get the pizza price")
if diametro:
    preco_previsto = modelo.predict([[diametro]])
    result = f'For a {int(diametro)} diameter pizza the price is $ {round(float(preco_previsto[0][0]),2)}  dollars'
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
