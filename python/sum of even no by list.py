a = [10, 15, 20, 7, 8, 13, 30]
even_sum=0
for i in range(len(a)):
    if a[i]%2==0:
        even_sum=even_sum+a[i]
print("Even sum =",even_sum)