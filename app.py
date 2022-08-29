import streamlit as st
from add_pages import pagess
from addpages import page1 as p1
from addpages import page2 as p2
from addpages import page3 as p3
from addpages import page4 as p4
#from addpages import page5 as p5

app=pagess()

st.title('movie')

app.add_page('메인페이지',p1.app)
app.add_page('영화정보',p2.app)
app.add_page('영화인정보',p3.app)
app.add_page('영화추천',p4.app)
#app.add_page('워드 클라우드',p5.app)
app.run()
