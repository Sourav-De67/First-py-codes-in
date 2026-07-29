a=input('Enter any string :')
checked=''
for ch in a:
    if ch not in checked:
        count=a.count(ch)
        print(f"count of {ch} is {count}")
    checked+=ch
