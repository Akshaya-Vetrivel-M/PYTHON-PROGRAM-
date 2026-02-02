name = input("Enter Student Name:")
roll = input ("Enter Roll Number:")
course = input ("Enter Course Name:")

print ("\nEnter marks out of 100:\n")
Sub1 = int(input ("Subject1 :"))
Sub2 = int(input ("Subject2 :"))
Sub3 = int(input ("Subject3 :"))
Sub4 = int(input ("Subject4 :"))
Sub5 = int(input ("Subject5 :"))

t=Sub1+Sub2+Sub3+Sub4+Sub5
percentage = t / 5

if  percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >=70:
    grade = "B+"
elif percentage >=60:
    grade = "B"
elif percentage >=50:
    grade = "C"
else:
    grade = "Fail"

print ("\n===================STUDENT MARKSHEET====================")
print ("Name : ", name)
print ("Roll Number: ", roll)
print ("Course :", course)

print ("---------------------------------------------------------")

print ("Subject 1 : ", Sub1)
print ("Subject 2 : ", Sub2)
print ("Subject 3 : ", Sub3)
print ("Subject 4 : ", Sub4)
print ("Subject 5 : ", Sub5)

print ("---------------------------------------------------------")

print ("Total Marks :" ,t)
print ("Percentage :" , percentage, "%")
print ("Grade :", grade)
print ("===========================================================")



O/P:
Enter Student Name:Akshaya
Enter Roll Number:004
Enter Course Name:CS

Enter marks out of 100:

Subject1 :98
Subject2 :95
Subject3 :88
Subject4 :90
Subject5 :85

===================STUDENT MARKSHEET====================
Name :  Akshaya
Roll Number:  004
Course : CS
---------------------------------------------------------
Subject 1 :  98
Subject 2 :  95
Subject 3 :  88
Subject 4 :  90
Subject 5 :  85
-----------------------------------------------
Total Marks : 456
Percentage : 91.2 %
Grade : A+
===========================================================
