s=input("Enter a string :")
words=s.split()
checked=''
for w in words:
    if w not in checked:
        print(w,end=' ')
        checked=checked+" "+w
