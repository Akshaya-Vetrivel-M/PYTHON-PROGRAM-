d=int(input ("Enter Number of days:"))
fine=0
if(d<=5):
  fine=d*0.50
  print("Fine : ",float(fine))
elif(d>5 and d<=10):
  i=d-5
  fine=(i*1)+(5*0.5)
  print("Fine : ",float(fine))
elif(d>10 and d<=30):
  i=d-10
  fine=(i*5)+(5*0.5)+(5*1)
  print("Fine : ",float(fine))
else:
  i=d-10
  fine=(i*5)+(5*0.5)+(5*1)
  print("Your Membership is cancelled ")
  print("Fine amount (Rs): ",float(fine))

o/p:
Enter Number of days:12
Fine :  17.5
