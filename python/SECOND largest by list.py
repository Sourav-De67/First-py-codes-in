a = [10, 45, 23, 67, 12]

large = 0
second = 0

for i in range(len(a)):
    if a[i] > large:
        second = large
        large = a[i]
    elif a[i] > second and a[i] != large:
        second = a[i]

print("Second largest =", second)