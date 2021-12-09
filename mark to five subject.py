physics=int(input("enter the phsics marks"))
chemistry=int(input("enter the chemistry marks"))
biology=int(input("enter the biology marks"))
maths=int(input("enter the maths marks"))
computer=int(input("enter the computer marks"))
total=(physics+chemistry+biology+maths+computer)
per=(total/500)*100
print=("percentage",per)
if per>=90:
    print("A grade")
elif per>=80:
    print("B grade")
elif per>=70:
    print("C grade")  
elif per>=60:
    print("D grade")  
elif per>=40:
    print("E grade")
else:
    print("F grade")





