import streamlit as st
import sqlite3

st.write('8/24일기준')
def app():
  
  connect = sqlite3.connect('box.db', isolation_level=None)
  cursor = connect.cursor();
  

  
  
  #input = 'SELECT 영화명,개봉일,img_url FROM box WHERE 개봉일 GROUP BY 영화명 BETWEEN 2202-07-24 AND 2202-08-24  ORDER BY 개봉일 DESC '
  
  input = 'SELECT 영화명,개봉일,img_url FROM box WHERE 개봉일 BETWEEN 1973-07-27 AND 2202-08-24 GROUP BY 영화명 ORDER BY 개봉일 DESC limit 5'
  input_1=cursor.execute(input)
  

  
  col1, col2, col3, col4, col5= st.columns(5)

  col_list=[col1,col2,col3,col4,col5]

  i=0

  for 영화명, 개봉일, img_url in input_1:
      with col_list[i]:
          st.image(img_url,width=130)
          st.write(영화명)
          st.write(개봉일)
      i+=1
      
      
  input_2 = 'SELECT 영화명,개봉일,img_url FROM box WHERE 개봉일 BETWEEN 1973-07-27 AND 2202-08-24 GROUP BY 영화명 ORDER BY 개봉일 DESC limit 5,5'
  col6, col7, col8, col9, col10 = st.columns(5)
  col_list_2=[col6, col7, col8, col9, col10]
  input_2=cursor.execute(input_2)
  j=0
  for 영화명, 개봉일, img_url in input_2:
      with col_list_2[j]:
          st.image(img_url,width=130)
          st.write(영화명)
          st.write(개봉일)
      j+=1
      




  
      
           
  
  
  #st.write(input)
  
  #quary_string = f"select 영화명, 개봉일, 순위, 누적관객수fantasy,peopleNm from box where movieNm in ('{영화제목}')"

  
  #cursor.execute(quary_string)
  #for test in cursor:
      #st.write(test)
      


      #st.image(img_url,width=300,)


