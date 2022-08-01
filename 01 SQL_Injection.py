#fragile to SQL Injection attack
import sys
import pymysql

if len(sys.argv) != 2:
    print("Invalid")
    sys.exit(1)

conn = pymysql.connect(
    host = host,
    user = 'root',
    password = 'password'
    port = 3306,
    db = 'bawpp',
    charset = 'utf8'
)

search_name = sys.argv(1)
cursor = conn.cursor()

s_query = "SELECT * FROM USERS WHERE name like '%" + search_name + "%'"

#execute
cursor.execute(sql_query)
result = cursor.fetchall()
s_format = '%-20s%-40s%-20s%-20s%-20s%-20s%-20s\n'
s_out = s_format %('ID', 'name', 'age', 'gender','address', 'date', 'check')

for data in result:
    s_out += s_format % (data[0], data[1], data[2], data[3], data[4], data[5], data[6])

print(s_out)

cursor.close()
conn.close()

# python search.py "man'or'a'='a'--" -> SQL Injection attack
# Defend SQL Injection attack
s_query = "SELECT * FROM USERS WHERE name like %s"
cursor.execute(s_query, ('%'+search_name+'%', ))
result = cursor.fetchall()




#fragile to SQK Injection
cursor.execute("SELECT admin FROM users WHERE username='"+username+"'")
cursor.execute("SELECT admin FROM users WHERE username='%s'"%username)
cursor.execute("SELECT admin FROM users WHERE username='{}'".format(username))

#Defend SQL Injection
cursor.execute("SELECT admin FROM users WHERE username = %s", (username, ))
cursor.execute("SELECT admin FROM users WHERE username = %(uname", {'uname':username})