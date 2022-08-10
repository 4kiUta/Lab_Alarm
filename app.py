import streamlit as st
import pandas as pd


st.write("""Hello 
I am Gladys & José
""")

st.write("""This is the begining
of all the cool things 
""")


## playing around
## for better charts might be needed to install 'plotly' module
data = pd.read_csv('data_gen/team_heart.csv')
st.area_chart(data=data['Age'])