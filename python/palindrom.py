a=int(input('Enter a number :'))
c=a
rev=0
while a>0:
    digit=a%10
    rev=rev*10+digit
    a=a//10
if c==rev:
    print("Palindrom")
else:
    print("Not palindrom")