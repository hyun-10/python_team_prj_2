import streamlit as st
import sqlite3
#connect = sqlite3.connect('movie_people_included_imgURL.db', isolation_level=None)
#connect = sqlite3.connect('streamlit_cloud_sqlite_test/blob/main/db/movie_people_included_imgURL.db', isolation_level=None)
#connect = sqlite3.connect('./db/movie_people_included_imgURL.db', isolation_level=None)
#connect = sqlite3.connect('../db/movie_people_included_imgURL.db', isolation_level=None)
connect = sqlite3.connect('db/test_1/movie_people_included_imgURL.db', isolation_level=None)




def app():
  connect = sqlite3.connect('movie_people_included_imgURL.db', isolation_level=None)
  cursor = connect.cursor();

  input = st.text_input("영화인 이름")
  quary_string = f"select peopleCd, peopleNmEn ,repRoleNm, peopleNm ,imgURL ,filmoNames ,peopleNm from movie_people_included_imgURL where peopleNm in ('{input}')"
  cursor.execute(quary_string)
  
  col1, col2 = st.columns(2,gap="small")
  for peopleCd, peopleNmEn ,repRoleNm, peopleNm ,imgURL ,filmoNames,peopleNm  in cursor:
      st.write(peopleNm, peopleNmEn)
      with col1 :
          st.image(imgURL,width=150,)
      with col2 :
          st.write(filmoNames)

      
