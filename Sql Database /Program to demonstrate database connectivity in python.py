import mysql.connector
conn = mysql.connector.connect(host='localhost', user='root', passwd='', database='db1')
cursor = conn.cursor()
cursor.execute("INSERT INTO books VALUES (101, 'Python')")
conn.commit()
print("Record inserted successfully")
cursor.execute("SELECT * FROM books")
result = cursor.fetchall()
print(result)
cursor.close()
conn.close()

O/P:
record inserted successfully
(101,’python’)
