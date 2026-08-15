n=int(input("Enter the number :"))
reverse=0
for i in str(n):
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
print('reversed number is ',reverse)