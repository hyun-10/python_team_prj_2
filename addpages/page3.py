import streamlit as st
import sqlite3

def app():
  connect = sqlite3.connect('db/3p/movie_people_included_imgURL.db', isolation_level=None)
  cursor = connect.cursor();

  input = st.text_input("영화인 이름")
  quary_string = f"select peopleCd, peopleNmEn ,repRoleNm, peopleNm ,imgURL ,filmoNames ,peopleNm from movie_people_included_imgURL where peopleNm in ('{input}')"
  cursor.execute(quary_string)
  
  col1, col2, col3= st.columns(3,gap="small")
  for peopleCd, peopleNmEn ,repRoleNm, peopleNm ,imgURL ,filmoNames,peopleNm  in cursor:
      if imgURL != None :
          #st.write(peopleNm)
          #else :
          #st.write(peopleNm, peopleNmEn)
          with col1 :
              st.image(imgURL,width=150,)
          with col2 :
              st.write(peopleNm,peopleNmEn)
          with col3 :
              st.write(filmoNames)

      
