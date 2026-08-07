def sum(n):
    total=0
    while n>0:
        digit=n%10
        total+=digit
        n=n//10
    print(total)
sum(1234)