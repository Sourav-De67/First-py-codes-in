number=[]
large=0
for i in range (5):
    n=int(input("Enter number :"))
    number.append(n)
for i in range(len(number)):
    if number[i]>large:
        large=number[i]
print(f"{large} is largest")