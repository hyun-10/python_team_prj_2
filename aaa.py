import sqlite3
import streamlit as st
connect = sqlite3.connect('movie_people_included_imgURL.db', isolation_level=None)

st.title('영화')
def app():
    connect = sqlite3.connect('movie_people_included_imgURL.db', isolation_level=None)

cursor = connect.cursor();
    st.title('영화')

    cursor = connect.cursor();

input = st.text_input("영화인 이름")

quary_string = f"select peopleCd, peopleNmEn ,repRoleNm, peopleNm ,imgURL ,filmoNames ,peopleNm from movie_people_included_imgURL where peopleNm in ('{input}')"
    input = st.text_input("영화인 이름")

    quary_string = f"select peopleCd, peopleNmEn ,repRoleNm, peopleNm ,imgURL ,filmoNames ,peopleNm from movie_people_included_imgURL where peopleNm in ('{input}')"



cursor.execute(quary_string)

for peopleCd, peopleNmEn ,repRoleNm, peopleNm ,imgURL ,filmoNames,peopleNm  in cursor:
    st.write(peopleNm, peopleNmEn)
    cursor.execute(quary_string)

    for peopleCd, peopleNmEn ,repRoleNm, peopleNm ,imgURL ,filmoNames,peopleNm  in cursor:
        st.write(peopleNm, peopleNmEn)

        st.write(filmoNames)

        st.image(imgURL,width=150,)

    st.write(filmoNames)

    st.image(imgURL,width=150,)
