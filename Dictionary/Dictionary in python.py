my_dict = {"Name" : "Akshaya" ,"Age" :18 ,"City" :"US"}
print(f"Name : {my_dict ['Name']}")
print (f"Age : {my_dict['Age']}")
print (f"City : {my_dict . get('City')}")
print (f"Occupation (of exists): {my_dict.get ('Occupation','Not specified')}")

o/p:
Name : Akshaya
Age : 18
City : US
Occupation (of exists): Not specified
