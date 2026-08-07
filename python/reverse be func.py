def rev(n):
    rev=0
    i=1
    while n>0:
        digit = n%10
        rev=rev*10+digit
        n=n//10
    print(f"the reverse of the number is {rev}")
rev(1234)