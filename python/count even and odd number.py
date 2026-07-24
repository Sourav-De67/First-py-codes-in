n=int(input('Enter a number :'))
even=0
odd=0
while n>0:
    digit=n%10
    if digit%2==0:
        even+=1
    else:
        odd+=1
    n=n//10
print(f"Even digit are {even} and odd digit are {odd}")
