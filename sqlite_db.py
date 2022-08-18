import sqlite3
import streamlit as st
connect = sqlite3.connect('all_movie_people_.db', isolation_level=None)

st.title('영화')

cursor = connect.cursor();


input = st.text_input("영화인 이름")


cursor.execute("""select peopleCd, peopleNmEn ,repRoleNm, filmoNames from all_movie_people_list where peopleNm in ('이훈')""")
for i in cursor:
    st.write(i)

