import sqlite3
import streamlit as st
connect = sqlite3.connect('movie_people_included_imgURL.db', isolation_level=None)

st.title('영화')

cursor = connect.cursor();


input = st.text_input("영화인 이름")

quary_string = f"select peopleCd, peopleNmEn ,repRoleNm, imgURL ,filmoNames from movie_people_included_imgURL where peopleNm in ('{input}')"




cursor.execute(quary_string)

for peopleCd, peopleNmEn ,repRoleNm, imgURL ,filmoNames in cursor:
    st.write(repRoleNm)
    st.image(
            "imgURL",
            width=400, # Manually Adjust the width of the image as per requirement
        )
