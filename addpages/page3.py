import streamlit as st
import sqlite3

def app():
  st.subheader('영화인 정보')
  connect = sqlite3.connect('db/3p/movie_people_included_imgURL.db', isolation_level=None)
  cursor = connect.cursor();

  input = st.text_input("영화인 이름")
  quary_string = f"select peopleCd, peopleNmEn ,repRoleNm, peopleNm ,imgURL ,filmoNames ,peopleNm from movie_people_included_imgURL where peopleNm in ('{input}')"
  cursor.execute(quary_string)
  
  col1, col2, col3= st.columns(3)
 
  
  col_list=[col1, col2,col3]
  j=0
  for peopleCd, peopleNmEn ,repRoleNm, peopleNm ,imgURL ,filmoNames,peopleNm  in cursor:
      #if peopleNmEn != None :
          #st.write(peopleNm)
          #else :
          #st.write(peopleNm, peopleNmEn)
      with col_list[0] :
          st.image(imgURL,width=150)
          st.write(peopleNm)
          st.write(filmoNames)


      j+=1

              

      
