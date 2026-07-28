a=int(input('Enter a number :'))
b=int(input('Enter a number :'))
c=a*b
while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
print(f"LCM is {c/a} ")
