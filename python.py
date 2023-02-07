import math
print("Baymolda Aruzhan")
print("3-курс")
age = int(input("Input:"))
if(age >18):
    print("adult")
elif(age<18):
    print("teenager or child ")
else:
    print("age is:",age)
print(math.pow(age,2))