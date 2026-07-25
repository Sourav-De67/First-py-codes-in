n=int(input('Enter a number :'))
r=0
while r<n:
    c=1
    while c<=2*r+1:
        print(r+1,end=' ')
        c+=1
    print()
    r+=1