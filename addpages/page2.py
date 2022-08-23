import streamlit as st
import sqlite3
st.write('영화정보 조회')


def app():
  connect = sqlite3.connect('movie.db', isolation_level=None)
  cursor = connect.cursor();
  
  Category1 = st.columns(5)
  Data_category = Category1[0].checkbox("가족") 


  Data_category1 = Category1[1].checkbox("공연") 
  Data_category2 = Category1[2].checkbox("공포") 
  
  Data_category3 = Category1[3].checkbox("다큐멘터리") 
  Data_category4 = Category1[4].checkbox("드라마")
  Category2 = st.columns(5)
  Data_category5 = Category2[0].checkbox("멜로")
  
  Data_category6 = Category2[1].checkbox("뮤지컬")
  Data_category7 = Category2[2].checkbox("미스터리")
  Data_category8 = Category2[3].checkbox("범죄")
  Data_category9 = Category2[4].checkbox("사극")
  Category3 = st.columns(5)
  Data_category10 = Category3[0].checkbox("서부극")
  Data_category11 = Category3[1].checkbox("성인물")
  Data_category12 = Category3[2].checkbox("스릴러")
  Data_category13 = Category3[3].checkbox("애니메이션")
  Data_category14 = Category3[4].checkbox("액션")
  Category4 = st.columns(5)
  Data_category15 = Category4[0].checkbox("어드벤처")
  Data_category16 = Category4[1].checkbox("전쟁")
  Data_category17 = Category4[2].checkbox("코미디")
  Data_category18 = Category4[3].checkbox("판타지")


  input = st.text_input('')

  
  #quary_string = f"select movieCd, movieNm, prdtYear, showTm, prdtStatNM, nations, family, performance, horror, etc, documentary, drama, melodrama, musical, mystery, crime, historical, western, adult, thriller, animated, action, adventure, war, comedy, fantasy,peopleNm, actors, staffs, img_url from movie where movieNm in ('{input}')"
  #quary_string = f"select movieNm, peopleNm,img_url from movie where movieNm in ('{input}') "
  #quary_string = "select movieNm, peopleNm,img_url from movie where movieNm like '%코난%' "

  if input:
      quary_string = f"select movieNm, peopleNm,img_url from movie where movieNm like '%{input}%' and family=='0' and performance=='0' and horror=='0' and etc=='0' and documentary=='0' and drama=='0' and melodrama=='0' and musical=='0' and mystery=='0' and crime=='0' and historical=='0' and western=='0' and adult=='0' and thriller=='0' and animated=='0' and action=='0' and adventure=='0' and war=='0'  and comedy=='0' and fantasy=='0' "
      cursor.execute(quary_string)
  for movieNm,peopleNm,img_url in cursor:

        st.image(img_url,width=130)
        st.write(movieNm, peopleNm)




'''
        if input:
        quary_string = "select movieNm, peopleNm,img_url family, performance, horror, etc, documentary, drama, melodrama, musical, mystery, crime, historical, western, adult, thriller, animated, action, adventure, war, comedy, fantasy from movie where movieNm like '%{0}%' "
        cursor.execute(quary_string)
    for movieNm,peopleNm,img_url in cursor:
        
        st.image(img_url,width=130)
        st.write(movieNm, peopleNm)
 
'''


      
