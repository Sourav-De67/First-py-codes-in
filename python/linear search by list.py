a = [10, 25, 34, 47, 56, 72]

search = int(input("Enter number to search: "))

found = False

for i in range(len(a)):
    if a[i] == search:
        print(f"{search} found at index {i}")
        found = True
        break

if not found:
    print(f"{search} not found")