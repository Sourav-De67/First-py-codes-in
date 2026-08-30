n = int(input("Enter the size of matrix: "))

a = []

print("Enter the elements:")
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    a.append(row)

symmetric = True
skew_symmetric = True

for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]:
            symmetric = False

        if a[i][j] != -a[j][i]:
            skew_symmetric = False

if symmetric:
    print("Matrix is Symmetric")
elif skew_symmetric:
    print("Matrix is Skew-Symmetric")
else:
    print("Matrix is neither Symmetric nor Skew-Symmetric")
