import sqlite3

connect = sqlite3.connect('C:/all_movie_people_.db', isolation_level=None)



cursor = connect.cursor();



select = """select peopleCd, peopleNmEn ,repRoleNm, filmoNames from all_movie_people_list where peopleNm in ('방준석')
"""
cursor.execute(select)
for i in cursor:
    print(i)
    
