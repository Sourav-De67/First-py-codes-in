def positive_negative(n):
    if n>0:
        return "positive"
    elif n<0:
        return "negative"
    else:
        return "zero"
result = positive_negative(0)
print(result)