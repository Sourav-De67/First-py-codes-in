'''a=int(input('Enter a number :'))
c=a
rev=0
while a>0:
    digit=a%10
    rev=rev*10+digit
    a=a//10
if c==rev:
    print("Palindrom")
else:
    print("Not palindrom")'''
def pall(a):
    rev=0
    c=a
    while a>0:
        digit=a%10
        rev=rev*10+digit
        a=a//10
    if c==rev:
        print("Palindrom")
    else:
        print("Not palindrom")
        
pall(121)
pall(142)