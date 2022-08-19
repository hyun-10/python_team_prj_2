import streamlit as st
import sqlite3
st.write('영화정보 조회')


def app():
  connect = sqlite3.connect('reset3.db', isolation_level=None)
  cursor = connect.cursor();
  
  Category = st.columns(19)
  Data_category = Category[0].checkbox("가족") 
  family = Data_category
  Data_category1 = Category[1].checkbox("공연") 
  Data_category2 = Category[2].checkbox("공포") 
  
  Data_category3 = Category[3].checkbox("다큐멘터리") 
  Data_category4 = Category[4].checkbox("드라마")

  Data_category5 = Category[5].checkbox("멜로")

  Data_category6 = Category[6].checkbox("뮤지컬")
  Data_category7 = Category[7].checkbox("미스터리")
  Data_category8 = Category[8].checkbox("범죄")
  Data_category9 = Category[9].checkbox("사극")

  Data_category10 = Category[10].checkbox("서부극")
  Data_category11 = Category[11].checkbox("성인물")
  Data_category12 = Category[12].checkbox("스릴러")
  Data_category13 = Category[13].checkbox("애니메이션")
  Data_category14 = Category[14].checkbox("액션")

  Data_category15 = Category[15].checkbox("어드벤처")
  Data_category16 = Category[16].checkbox("전쟁")
  Data_category17 = Category[17].checkbox("코미디")
  Data_category18 = Category[18].checkbox("판타지")
  
  cols = ["가족", "공연", "공포", "다큐멘터리", "드라마",'멜로','뮤지컬','미스터리','범죄','사극','서부극','성인물','스릴러','서부극','성인물','스릴러','액션','어드벤처','전쟁','코미디'.'판타지']
  st_ms = st.multiselect("Columns", df.columns.tolist(), default=cols)
  
  
  input = st.text_input("영화 이름")
  quary_string = f"select movieCd, movieNm, prdtYear, showTm, prdtStatNM, nations, family, performance, horror, etc, documentary, drama, melodrama, musical, mystery, crime, historical, western, adult, thriller, animated, action, adventure, war, comedy, fantasy,peopleNm, actors, staffs from movie_list where movieNm in ('{input}')"
  cursor.execute(quary_string)
  for 영화이름 in cursor:

      
      st.write(영화이름)

      #st.image(img_url,width=300,)
