
'''n=int(input("Enter the number :"))
for i in range(1,n+1):
    if i%2!=0:
        print(i)'''
      #  multiplication table
'''n=int(input("Enter the number :"))
for i in range (1,11):
    print(f"{n}*{i}={n*i}")'''
#factorial
'''n=int(input("Enter the number :"))
fact=1
for i in range (1,n+1):
    fact=fact*i
print('factorial =',fact)'''
#counting number of digit
'''n=int(input("Enter the number :"))
count=0
if n==0:
    count=1
else:
    n=abs(n)
    for i in str(n):
        n=n//10
        count+=1
print('number of digit is ',count)'''
#reverse of a number
'''n=int(input("Enter the number :"))
reverse=0
for i in str(n):
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
print('reversed number is ',reverse)'''
#checking prime number
'''n=int(input("Enter the number :"))
c=0
for i in range (1,n+1):
    if n%i==0:
        c+=1
if c==2:
     print('prime')
else:
    print('not prime')'''
#pattern printing
'''n=int(input("Enter the number :"))
for i in range (1,n+1):
    for j in range (1,i+1):
        print('*',end="")
    print()'''
#number pattern
'''n=int(input("Enter the number :"))
for i in range (1,n+1):
    for j in range (1,i+1):
        print(j,end="")
    print()'''
#largest number
'''n=int(input("Enter how many number you  want :"))
largest=int(input("Enetr the number 1:"))
for i in range(2,n+1):
    num=int(input(f"Enter the number {i} :"))
    if num>largest:
        largest = num
print('the largest number is',largest)'''
