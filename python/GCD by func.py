def gcd(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
result=gcd(12,18)
print("GCD is ",result)