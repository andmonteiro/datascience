import streamlit as st
import pandas as pd

file = r'C:\Users\Anderson\Desktop\listings.csv'
@st.cache

def load_data():
    columns = {"latitude": "lat", "longitude": "lon"}
    df = pd.read_csv(file)
    df = df.rename(columns=columns)
    return df

df = load_data()

st.title("Airbnb em Lisboa")
st.markdown(
    """
    Dashboard para análise de locação atráves do airbnb
    """
)

st.sidebar.header("Configurações")
if st.sidebar.checkbox("Mostrar tabela"):
    st.markdown("## Tabela de Dados")
    st.write(df)

price = st.sidebar.slider("Veja os imóveis pelo valor de locação.", 0,192, 100)
room_types = df.room_type.unique()
room_types_selected = st.sidebar.multiselect("Selecione o tipo de imóvel:", room_types)

if not room_types_selected:
    room_types_selected = df.room_type.unique()

st.map(df[(df['price'] == price) & (df["room_type"].isin(room_types_selected))])