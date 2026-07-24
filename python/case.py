ch=input('Enter a single charecter: ')
if len(ch)!=1:
    print("Enter a single charecter")
elif ch.isupper():
    print(f"{ch} is a upper case charecter")
elif ch.islower():
    print(f"{ch} is a lower case charecter")
elif ch.isdigit():
    print(f"{ch} is a digit")
else:
    print(f"{ch} is symbol or a special charecter")
