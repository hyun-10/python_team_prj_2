import sqlite3
import streamlit as st
connect = sqlite3.connect('all_movie_people_.db', isolation_level=None)



cursor = connect.cursor();

st.write('영화인 검색')
input = st.text_input("영화인")
globals()[input]=input

cursor.execute("""select peopleCd, peopleNmEn ,repRoleNm, filmoNames from all_movie_people_list where peopleNm in (input)""")
for i in cursor:
    st.write(i)

