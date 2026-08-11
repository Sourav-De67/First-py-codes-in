number=[]
even=0
odd=0
for i in range (5):
    n=int(input("Enter number :"))
    number.append(n)
for i in range (5):
    if number[i]%2==0:
        even+=1
    else:
        odd+=1
print(f"even numbers are {even} and odd numbers are {odd}")