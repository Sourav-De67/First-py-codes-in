def lcm(a,b):
    c=a*b
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return c/a
result=lcm(12,36)
print("LCM is ",result)