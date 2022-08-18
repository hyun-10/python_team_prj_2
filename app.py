import streamlit as st
import add_pages









app=pages()

st.title('Movie Project')

app.add_page('메인 페이지')
app.add_page('영화 정보')
app.add_page('영화인 정보', p3.app)
app.add_page('영화추천')
app.add_page('가상 캐스팅')
