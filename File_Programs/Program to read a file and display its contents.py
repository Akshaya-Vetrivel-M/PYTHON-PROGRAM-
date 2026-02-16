f=open('myfile.txt','w')
f.write('My first file')
f.close()
f=open('myfile.txt','a')
f.write('\nWelcome Every one')
f.write('\nAppend Mode')
f.close()
f=open('myfile.txt','r')
print(f.read())
f.close()

O/P:
My first file
Welcome Every one
Append Mode
