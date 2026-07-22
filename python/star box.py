i=1
while i<=9:
    j=1
    while j<=9:
        if i==1 or i==9 or j==1 or j==9:
            print("* ",end='')
        else:
            print("  ",end='')
        j+=1
    print()
    i+=1