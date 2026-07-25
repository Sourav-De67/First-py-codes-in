n=int(input('Enter a number :'))
r=1
while r<=n:
    space=1
    while space<=n-r:
        print('',end=' ')
        space+=1
    c=1
    while c<=r:
        print(r,end=' ')
        c+=1
    print()
    r+=1
        
        
