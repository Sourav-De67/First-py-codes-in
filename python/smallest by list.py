number=[]
small=999999
for i in range (5):
    n=int(input("Enter number :"))
    number.append(n)
for i in range(len(number)):
    if number[i]<small:
        small=number[i]
print(f"{small} is smallest")
