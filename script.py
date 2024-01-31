import streamlit as st
import pandas as pd

st.write("""# Sales Model
          Abaixo encontram-se as predições de vendas para esse cliente.
          """)

df = pd.read_csv(".\\data\\Details.csv")

window = st.slider("Razão Montante/Quantidade:")


# Selecionando as colunas a serem exibidas
selected_columns = ['Amount', 'Quantity'] 

# Verificando se todas as colunas selecionadas são numéricas
for col in selected_columns:
    if df[col].dtype not in ['int64', 'float64']:
        st.error(f"A coluna {col} não é numérica. Por favor, converta-a em numérica ou selecione outra coluna.")
        break
else:
    st.line_chart(df[selected_columns])
