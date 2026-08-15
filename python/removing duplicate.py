a = [1, 2, 3, 2, 4, 5, 1, 6, 3]

result = []

for i in range(len(a)):
    duplicate = False

    for j in range(len(result)):
        if a[i] == result[j]:
            duplicate = True

    if not duplicate:
        result.append(a[i])

print(result)