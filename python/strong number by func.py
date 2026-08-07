def strong(n):
    temp=n
    total =0
    while temp>0:
        digit=temp%10
        fact=1
        i=1
        while i<=digit:
            fact=fact*i
            i+=1
        total=total+fact
        temp=temp//10
    if total==n:
        print(f"{n} is a strong number ")
    else:
        print(f"{n} is not a strong number ")

strong(145)