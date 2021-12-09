year=int(input("enter the leap year"))
if year%400==0:
    print(year,"is a leap year")
elif year%4==0 or year%100!=0:
    print(year,"is a leap year")
else:
    print(year,"is not leap year")