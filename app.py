import streamlit as st
import pandas as pd

# Criar um DataFrame de exemplo
data = {
    'Nome': ['Alice', 'Bob', 'Carlos', 'Diana'],
    'Idade': [25, 30, 35, 28],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
}

df = pd.DataFrame(data)

# Exibir no Streamlit
st.title("Exemplo de DataFrame no Streamlit")
st.write("Aqui está o DataFrame de exemplo:")
st.dataframe(df)

# Mostrar estatísticas descritivas como exemplo adicional
st.write("Estatísticas descritivas:")
st.write(df.describe())
