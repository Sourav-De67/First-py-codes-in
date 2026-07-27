n = int(input("Enter a number: "))

temp = n
total = 0

while temp > 0:
    digit = temp % 10

    fact = 1
    i = 1

    while i <= digit:
        fact = fact * i
        i += 1

    total = total + fact
    temp = temp // 10

if total == n:
    print("Strong Number")
else:
    print("Not a Strong Number")
