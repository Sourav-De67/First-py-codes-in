s=input("Enter a string :")
words=s.split()
max=0
large=""
for w in words:
    if len(w)>max:
        max=len(w)
        large=w
print(large)
