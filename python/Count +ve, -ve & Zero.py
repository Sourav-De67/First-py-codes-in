a=[ 10, -5, 0, 7, -2]
positive=0
negative=0
zero=0
for i in range(len(a)):
    if a[i]>0:
        positive+=1
    elif a[i]<0:
        negative+=1
    else:
        zero+=1
print("positive = ",positive)
print("negative = ",negative)
print("zero = ",zero)