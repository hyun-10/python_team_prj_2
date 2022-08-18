import streamlit as st
import sqlite3
connect = sqlite3.connect('movie_people_included_imgURL.db', isolation_level=None)

st.title('영화인 정보 조회')



def app():
  connect = sqlite3.connect('movie_people_included_imgURL.db', isolation_level=None)
  cursor = connect.cursor();

  input = st.text_input("영화인 이름")
  quary_string = f"select peopleCd, peopleNmEn ,repRoleNm, peopleNm ,imgURL ,filmoNames ,peopleNm from movie_people_included_imgURL where peopleNm in ('{input}')"
  cursor.execute(quary_string)
  
  for peopleCd, peopleNmEn ,repRoleNm, peopleNm ,imgURL ,filmoNames,peopleNm  in cursor:
      st.write(peopleNm, peopleNmEn)
      
      st.write(filmoNames)

      st.image(imgURL,width=150,)
