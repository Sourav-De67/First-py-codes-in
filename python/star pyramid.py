n = 5
i = 1
while i <= n:
    # Loop to print spaces
    space = 1
    while space <= n - i:
        print(" ", end='')
        space += 1
        
    # Loop to print stars
    j = 1
    while j <= i:
        print("* ", end='')
        j += 1
        
    print()
    i += 1