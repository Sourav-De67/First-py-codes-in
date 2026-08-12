a=[1,1,1,2,2,1,3,3,4,4,5,4,4,5,6,7,9,7,5,6,5,5,7,8,7]
search = int(input("Enter number to search: "))
count=0
for i in a:
    if i == search:
        count += 1
print(count)