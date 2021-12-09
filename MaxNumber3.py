# Inputs three no. and displays the largest

a=int(input("enter the first number"))   
b=int(input("enter the second numbr"))
c=int(input("enter the seccond number"))
if a>b and a>c:
    print("a is maximum")
elif b>a and b>c:
    print("b is maximum")
else:
    print("c is maximum")