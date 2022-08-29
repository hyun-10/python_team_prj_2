import streamlit as st
import sqlite3

def app():
  connect = sqlite3.connect('db/3p/movie_people_included_imgURL.db', isolation_level=None)
  cursor = connect.cursor();

  input = st.text_input("영화인 이름")
  quary_string = f"select peopleCd, peopleNmEn ,repRoleNm, peopleNm ,imgURL ,filmoNames ,peopleNm from movie_people_included_imgURL where peopleNm in ('{input}')"
  cursor.execute(quary_string)
  
  col1, col2, col3= st.columns(3)
  col_list=[col1, col2,col3]
  j=0
  for peopleCd, peopleNmEn ,repRoleNm, peopleNm ,imgURL ,filmoNames,peopleNm  in cursor:
      if imgURL != 'https://ssl.pstatic.net/static/movie/2012/06/dft_img120x150.png' and imgURL != 'https://ssl.pstatic.net/static/movie/2012/06/dft_img77x96_1.png' :
          #st.write(peopleNm)
          #else :
          #st.write(peopleNm, peopleNmEn)
          with col_list[0] :
              st.image(imgURL,width=150)

          with col_list[1] :
              st.image('',width=150)
              st.write(peopleNm,peopleNmEn,width=150)
          with col_list[2] :
              st.write(filmoNames,width=150)
          j+=1

              

      
