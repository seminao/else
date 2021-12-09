age1=int(input("age of first person"))
age2=int(input("age of second person"))
age3=int(input("age of third person"))
if age1>age2 and age1>age3:
    print(age1,'oldest')
elif age2>age3 and age2<age1:
    print(age2,"younger")
elif age3<age2 and age3<age1:
    print(age3,'youngest')
else:
    print("all are older")
