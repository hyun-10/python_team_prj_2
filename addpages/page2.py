import streamlit as st
import sqlite3
st.write('영화정보 조회')


def app():
  connect = sqlite3.connect('reset3.db', isolation_level=None)
  cursor = connect.cursor();
  
  Category = st.columns(5)
  Data_category = Category[0].checkbox("가족") 
  
  Data_category1 = Category[1].checkbox("공연") 
  Data_category2 = Category[2].checkbox("공포") 
  
  Data_category3 = Category[3].checkbox("다큐멘터리") 
  Data_category4 = Category[4].checkbox("드라마")
  Category = st.columns(5:10)
  Data_category5 = Category[5].checkbox("멜로")
 
  Data_category6 = Category[6].checkbox("뮤지컬")
  Data_category7 = Category[7].checkbox("미스터리")
  Data_category8 = Category[8].checkbox("범죄")
  Data_category9 = Category[9].checkbox("사극")
  Category = st.columns(5)

  
  
  input = st.text_input("영화 이름")
  quary_string = f"select movieCd, movieNm, prdtYear, showTm, prdtStatNM, nations, family, performance, horror, etc, documentary, drama, melodrama, musical, mystery, crime, historical, western, adult, thriller, animated, action, adventure, war, comedy, fantasy,peopleNm, actors, staffs from movie_list where movieNm in ('{input}')"
  cursor.execute(quary_string)
  for 영화이름 in cursor:

      
      st.write(영화이름)

      #st.image(img_url,width=300,)
