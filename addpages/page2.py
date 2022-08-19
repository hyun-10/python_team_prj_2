import streamlit as st
import sqlite3
st.write('영화정보 조회')


def app():
  connect = sqlite3.connect('movie_url_2000.db', isolation_level=None)
  cursor = connect.cursor();
  
  input = st.text_input("영화 이름")
  quary_string = f"select img_url, movie_t from url_2000 where movie_t in ('{input}')"
  cursor.execute(quary_string)
  for img_url, movie_t in cursor:

      
      st.write(movie_t)

      st.image(img_url,width=300,)
