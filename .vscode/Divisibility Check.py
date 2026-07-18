n=int(input("enter a number :"))
if n%3==0 and n%5==0:
    print(f"{n} is divisible by both 3 and 5")
elif n%3==0:
    print(f"{n} is divisible by only 3")
elif n%5==0:
    print(f"{n} is divisible by only 5")
else:
    print('not divisible by both')