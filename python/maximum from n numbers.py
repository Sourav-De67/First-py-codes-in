n=int(input('Enter a number :'))
print(f"{n} number will be entered")
max=0
for i in range(1,n+1):
    a=int(input(f"Enter number {i} :"))
    if a>max:
        max=a
print("maximum number is ",max)