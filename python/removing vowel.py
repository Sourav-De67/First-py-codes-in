a=input('Enter any string :')
v='aeiouAEIOU'
for ch in a :
    if ch not in v :
        print(ch,end='')
