a=[10,-20,30,-40,-3,4,5,6,-7,-9]
positive=[]
negative=[]
for i in a:
    if i>0:
        positive.append(i)
    else:
        negative.append(i)
positive=tuple(positive)
negative=tuple(negative)
print("positive numbers tuple",positive)
print("Negative numbers tuple",negative)
