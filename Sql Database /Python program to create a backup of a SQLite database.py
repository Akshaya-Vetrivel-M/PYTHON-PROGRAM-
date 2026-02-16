import sqlite3
import io
conn = sqlite3.connect('mydatabase.db')
with io.open('clientes_dump.sql', 'w') as f:
   for linha in conn.iterdump():
       f.write('%s\n' % linha)
print('Backup performed successfully.')
print('Saved as mydatabase_dump.sql')
conn.close()


Output:
Backup performed successfully.
Saved as mydatabase_dump.sql
