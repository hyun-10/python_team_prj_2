import streamlit as st
from add_pages import pages
from pages import pages3 as p3








app=pages()

st.title('Movie Project')
st.add_page('영화인 정보',p3.app)

