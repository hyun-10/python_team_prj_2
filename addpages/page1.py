import streamlit as st
import sqlite3



def app():
  connect = sqlite3.connect('box.db', isolation_level=None)
  cursor = connect.cursor();
  
  #cursor.execute('select 영화명 from box')
  #for i in cursor:
      #st.write(i)
  
  
  #input="select 영화명, 순위, 개봉일, 누적관객수, img_url from box ORDER BY 개봉일 DESC where 영화명 NOT IN(' " " ')"
  input="select 영화명, 순위, 개봉일, 누적관객수, img_url from box where 영화명 NOT IN(' " " ') ORDER BY 개봉일 DESC "
  cursor.execute(input)
  for i in cursor:
      st.write(i)
  
  
  
  
  #st.write(input)
  
  #quary_string = f"select 영화명, 개봉일, 순위, 누적관객수fantasy,peopleNm from box where movieNm in ('{영화제목}')"

  
  #cursor.execute(quary_string)
  #for test in cursor:
      #st.write(test)
      


      #st.image(img_url,width=300,)
