n=int(input('Enter a number :'))
i=1
total=0
while i<n:
    if n%i==0:
        total+=i
    i+=1
if total==n:
    print("Perfect number")
else:
    print("Not a perfect number")