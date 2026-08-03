a=[11,22,33,44,55,61,60]
greatest=a[0]
sec_larg=a[0]
for i in a:
    if i>greatest:
        sec_larg=greatest
        greatest=i
    elif i>sec_larg:
        sec_larg=i
print(sec_larg,greatest)