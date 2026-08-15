n=int(input("Enter how many number you  want :"))
largest=int(input("Enetr the number 1:"))
for i in range(2,n+1):
    num=int(input(f"Enter the number {i} :"))
    if num>largest:
        largest = num
print('the largest number is',largest)