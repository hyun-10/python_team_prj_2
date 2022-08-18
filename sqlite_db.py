import sqlite3

connect = sqlite3.connect('all_movie_people_.db', isolation_level=None)

st.write('test1')

cursor = connect.cursor();

st.write('test2')

select = """select peopleCd, peopleNmEn ,repRoleNm, filmoNames from all_movie_people_list where peopleNm in ('방준석')
"""
cursor.execute(select)
for i in cursor:
    st.write(i)

st.write('test3')
