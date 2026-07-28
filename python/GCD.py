a=int(input('Enter a number :'))
b=int(input('Enter a number :'))
while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
print("GCD is ", a)
