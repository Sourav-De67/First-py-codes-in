p=input("Enter your password :")
upper=lower=digit=special=0
for ch in p:
    if ch.isupper():
        upper=1
    elif ch.islower():
        lower=1
    elif ch.isdigit():
        digit=1
    else:
        special=1
if upper and lower and digit and special and len(p)>=8 and len(p)<=12:
    print("Valid password")
else:
    print("Invalid password")