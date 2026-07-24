n1=float(input("Enter first number :"))
n2=float(input("Enter second number :"))
print('1.Addition 2.substraction 3.Multiplication 4.Divition')
choice=int(input("Enter your choice :"))
if choice==1:
    print(f"{n1}+{n2}={n1+n2}")
elif choice==2:
    print(f"{n1}-{n2}={n1-n2}")
elif choice==3:
    print(f"{n1}*{n2}={n1*n2}")
elif choice==4:
    print(f"{n1}/{n2}={n1/n2}")
else:
    print('invalid choice!')