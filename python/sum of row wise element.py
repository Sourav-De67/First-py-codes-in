r = int(input("Enter the NUMBER OF Rows: "))
c= int(input("Enter the NUMBER OF columns: "))

a = []

print("Enter the elements:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    a.append(row)
for i in range(r):
    total=0
    for j in range(c):
        total=total+a[i][j]
    print("sum of rows",i+1,"=",total)