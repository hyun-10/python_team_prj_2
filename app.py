import streamlit as st
from add_pages import pagess
from pages import page1 as p1



app=pagess()

st.title('movie')

app.add_page('영화인정보',p1.app)

