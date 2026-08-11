number=[]
even=0
odd=0
for i in range (5):
    n=int(input("Enter number :"))
    number.append(n)
for i in range(len(number)-1,-1,-1):
    print(number[i])