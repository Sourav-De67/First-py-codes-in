def largest_digit(n):
    large=0
    while n>0:
        digit=n%10
        n=n//10
        if digit>large:
            large=digit
    return large
result=largest_digit(13973)
print(result)