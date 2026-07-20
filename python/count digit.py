n=int(input('Enter numbers : '))
count=0
if n==0:
    print('number of digit is 1')
else:
    while n>0:
        n=n//10
        count=count+1
    print('Number of digit is',count)