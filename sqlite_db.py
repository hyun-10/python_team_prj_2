import sqlite3

connect = sqlite3.connect('all_movie_people_.db', isolation_level=None)

print('test1')

cursor = connect.cursor();

print('test2')

select = """select peopleCd, peopleNmEn ,repRoleNm, filmoNames from all_movie_people_list where peopleNm in ('방준석')
"""
cursor.execute(select)
for i in cursor:
    print(i)

print('test3')
