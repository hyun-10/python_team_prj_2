import streamlit as st
import sqlite3
st.write('영화정보 조회')


def app():
  connect = sqlite3.connect('reset3.db', isolation_level=None)
  cursor = connect.cursor();
  
  Category = st.columns(4)
  Data_category = Category[0].checkbox("코미디") 
  Data_category1 = Category[1].checkbox("가족") 
  Data_category2 = Category[2].checkbox("액션") 
  Data_category3 = Category[3].checkbox("로맨스") 
  Data_category4 = Category[0].checkbox("") 
  
  
  input = st.text_input("영화 이름")
  quary_string = f"select movieCd, movieNm, prdtYear, showTm, prdtStatNM, nations, family, performance, horror, etc, documentary, drama, melodrama, musical, mystery, crime, historical, western, adult, thriller, animated, action, adventure, war, comedy, fantasy,peopleNm, actors, staffs from movie_list where movieNm in ('{input}')"
  cursor.execute(quary_string)
  for 영화이름 in cursor:

      
      st.write(영화이름)

      #st.image(img_url,width=300,)
