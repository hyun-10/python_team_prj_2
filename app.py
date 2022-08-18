import streamlit as st
from add_pages import pagess
from pages import page1 as p1



app=pagess()

st.title('movie')

app.add_page('메인페이지',p1.app)
app.run()
