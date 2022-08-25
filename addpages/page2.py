import streamlit as st
import sqlite3
st.write('영화정보 조회')


def app():
  connect = sqlite3.connect('db/2p/movie.db', isolation_level=None)
  cursor = connect.cursor()
    
  def and_(inputs,checker):


    quary_string = f"select movieNm, peopleNm,img_url from movie where movieNm like '%{inputs}%'"
    input_string = ['family','performance' ,'horror','etc','documentary','drama','melodrama','musical','mystery','crime','historical','western','adult','thriller','animated','action','adventure','war','comedy','fantasy']
    for key in checker.keys() :
        if checker[key] == 1 :
	        quary_string += f" and {input_string[key]}==1"
    
    cursor.execute(quary_string)

    for movieNm,peopleNm,img_url in cursor:
        st.image(img_url,width=130)
        st.write(movieNm, peopleNm)


  Data_categorys = dict()
  Data_checker = dict()
  for count in range(19) :
    Data_checker[count] = 0

  Category1 = st.columns(5)
  Data_categorys00 = Category1[0].checkbox("가족") 
  Data_categorys01 = Category1[1].checkbox("공연") 
  Data_categorys02 = Category1[2].checkbox("공포") 
  Data_categorys03 = Category1[3].checkbox("기타") 
  Data_categorys04 = Category1[4].checkbox("다큐멘터리") 
  Category2 = st.columns(5)
  Data_categorys05 = Category2[0].checkbox("드라마")
  Data_categorys06 = Category2[1].checkbox("멜로")
  Data_categorys07 = Category2[2].checkbox("뮤지컬")
  Data_categorys08 = Category2[3].checkbox("미스터리")
  Data_categorys09 = Category2[4].checkbox("범죄")
  Category3 = st.columns(5)
  Data_categorys10 = Category3[0].checkbox("사극")
  Data_categorys11 = Category3[1].checkbox("서부극")
  Data_categorys12 = Category3[2].checkbox("성인물")
  Data_categorys13 = Category3[3].checkbox("스릴러")
  Data_categorys14 = Category3[4].checkbox("애니메이션")
  Category4 = st.columns(5)
  Data_categorys15 = Category4[0].checkbox("액션")
  Data_categorys16 = Category4[1].checkbox("어드벤처")
  Data_categorys17 = Category4[2].checkbox("전쟁")
  Data_categorys18 = Category4[3].checkbox("코미디")
  Data_categorys19 = Category4[4].checkbox("판타지")

  Data_categorys[0] = Data_categorys00 
  Data_categorys[1] = Data_categorys01 
  Data_categorys[2] = Data_categorys02 
  Data_categorys[3] = Data_categorys03 
  Data_categorys[4] = Data_categorys04 
  Data_categorys[5] = Data_categorys05 
  Data_categorys[6] = Data_categorys06 
  Data_categorys[7] = Data_categorys07 
  Data_categorys[8] = Data_categorys08 
  Data_categorys[9] = Data_categorys09 
  Data_categorys[10] = Data_categorys10 
  Data_categorys[11] = Data_categorys11 
  Data_categorys[12] = Data_categorys12 
  Data_categorys[13] = Data_categorys13 
  Data_categorys[14] = Data_categorys14 
  Data_categorys[15] = Data_categorys15 
  Data_categorys[16] = Data_categorys16 
  Data_categorys[17] = Data_categorys17 
  Data_categorys[18] = Data_categorys18 
  Data_categorys[19] = Data_categorys19 

  for count in range(19) :
    if Data_categorys[count]:
        Data_checker[count]=1
    else :
        Data_checker[count]=0

  inputs = st.text_input('')
  if inputs:
    
    and_(inputs,Data_checker)



      
