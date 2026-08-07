def smallest_digit(n):
    small=9
    while n>0:
        digit=n%10
        n=n//10
        if digit<small:
            small=digit
    return small
result=smallest_digit(13973)
print(result)