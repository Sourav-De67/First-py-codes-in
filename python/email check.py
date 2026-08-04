e=input("Enter a email :")
p=e.find("@")
if e[p:] =="@gmail.com":
    print(f"{e} is a valid email")
else:
    print(f"{e} is not a valid email")