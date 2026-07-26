n=int(input('Enter numbers :'))
largest=0
while n>0:
    digit=n%10
    if digit>largest:
        largest=digit
    n=n//10
print("largest digit is ",largest)
