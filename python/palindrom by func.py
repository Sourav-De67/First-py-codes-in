def pal(n):
    rev=0
    c=n
    while n>0:
        digit = n%10
        rev=rev*10+digit
        n=n//10
    if rev==c:
        print(f"{c} is a palindrome")
    else:
        print(f"{c} is not a palindrome")
pal(123)