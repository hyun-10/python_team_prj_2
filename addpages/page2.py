import streamlit as st
import sqlite3
st.write('영화정보 조회')


def app():
  connect = sqlite3.connect('reset3.db', isolation_level=None)
  cursor = connect.cursor();
  
  Category = st.columns(4)
  Data_category = Category[0].checkbox("가족") 
  Data_category1 = Category[1].checkbox("공연") 
  Data_category2 = Category[2].checkbox("공포") 
  Data_category3 = Category[3].checkbox("다큐멘터리") 
  Data_category4 = Category[4].checkbox("드라마")
  Data_category4 = Category[5].checkbox("멜로")
  Data_category4 = Category[6].checkbox("뮤지컬")
  Data_category4 = Category[7].checkbox("미스터리")
  Data_category4 = Category[8].checkbox("범죄")
  Data_category4 = Category[9].checkbox("사극")
  Data_category4 = Category[10].checkbox("서부극")
  Data_category4 = Category[11].checkbox("성인물")
  Data_category4 = Category[12].checkbox("스릴러")
  Data_category4 = Category[13].checkbox("애니메이션")
  Data_category4 = Category[14].checkbox("액션")
  Data_category4 = Category[15].checkbox("어드벤처")
  Data_category4 = Category[16].checkbox("전쟁")
  Data_category4 = Category[17].checkbox("코미디")
  Data_category4 = Category[18].checkbox("판타지")
  
  
  
  input = st.text_input("영화 이름")
  quary_string = f"select movieCd, movieNm, prdtYear, showTm, prdtStatNM, nations, family, performance, horror, etc, documentary, drama, melodrama, musical, mystery, crime, historical, western, adult, thriller, animated, action, adventure, war, comedy, fantasy,peopleNm, actors, staffs from movie_list where movieNm in ('{input}')"
  cursor.execute(quary_string)
  for 영화이름 in cursor:

      
      st.write(영화이름)

      #st.image(img_url,width=300,)
