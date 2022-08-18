import streamlit as st
st.write('영화정보 조회')


def app():
  connect = sqlite3.connect('movie_value_test1.db', isolation_level=None)
  cursor = connect.cursor();
  
  input = st.text_input("영화 이름")
  quary_string = f"select peopleCd, peopleNmEn ,repRoleNm, peopleNm ,imgURL ,filmoNames ,peopleNm from movie_people_included_imgURL where peopleNm in ('{input}')"
  cursor.execute(quary_string)
