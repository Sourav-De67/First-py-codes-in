n=int(input('Enter a number :'))
temp =n
digits =len(str(n))
total =0
while temp>0:
    digit =temp%10
    total =total+digit**digits
    temp=temp//10
if total==n:
    print("Armstrong number")
else:
    print("Not an armstrong number")
