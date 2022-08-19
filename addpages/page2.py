import streamlit as st
import sqlite3
st.write('영화정보 조회')


def app():
  connect = sqlite3.connect('reset3.db', isolation_level=None)
  cursor = connect.cursor();
  
  input = st.text_input("영화 이름")
  quary_string = f"select 영화이름 from movie where 영화이름 in ('{input}')"
  cursor.execute(quary_string)
  for 영화이름 in cursor:

      
      st.write(영화이름)

      #st.image(img_url,width=300,)
