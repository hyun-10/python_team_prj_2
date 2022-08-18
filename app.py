import streamlit as st
from add_pages import pages
from pages import pages3 as p1
from pages import pages3 as p2
from pages import pages3 as p3
from pages import pages3 as p4
from pages import pages3 as p5








app=pages()

st.title('Movie Project')
st.add_page('메인 페이지')
st.add_page('영화 정보')
st.add_page('영화인 정보',p3.app)
st.add_page('영화추천')
st.add_page('가상 캐스팅')


