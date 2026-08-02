def arms(n):
    total=0
    temp=n
    digits=len(str(n))
    while n>0:
        digit=n%10
        total=total+digit**digits
        n=n//10
    if total==temp:
        return "Armstrong"
    else:
        return "Not armstrong"
result=arms(153)
print(result)