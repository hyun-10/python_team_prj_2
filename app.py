import streamlit as st
from add_pages import pages









app=pages()

st.title('Movie Project')


app.add_page('영화인 정보', p3.app)

app.run()
