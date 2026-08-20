a = [12, 7, 5, 18, 20, 13, 9, 24]

even=[]
odd=[]

for i in range(len(a)):
    if a[i]%2==0:
        even.append(a[i])
    else:
       odd.append(a[i])

print(even)
print(odd)