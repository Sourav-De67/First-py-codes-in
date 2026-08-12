a=[1,1,1,2,2,1,3,3,4,4,5,4,4,5,6,7,9,7,5,6,5,5,7,8,7]
d={}
for i in a :
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
print(d)
