Pip install pysqlite3
import sqlite3
conn = sqlite3.connect("school.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS Students(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Age INTEGER,
    Grade TEXT
)
""")
data = [("Alice", 20, "A"), ("Bob", 21, "B")]
cur.executemany("INSERT INTO Students (Name, Age, Grade) VALUES (?, ?, ?)", data)
conn.commit()
print("Students:")
for row in cur.execute("SELECT * FROM Students"):
    print(row)
cur.execute("DELETE FROM Students WHERE ID = 1")
conn.commit()
print("\nAfter Deletion:")
for row in cur.execute("SELECT * FROM Students"):
    print(row)
conn.close()  

O/P:
Students:
(1, 'Alice', 20, 'A')
(2, 'Bob', 21, 'B')
After Deletion:
(2, 'Bob', 21, 'B')
