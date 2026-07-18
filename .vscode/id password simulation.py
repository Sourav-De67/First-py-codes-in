correct_userid="sourav1234"
correct_password="12345"
userid=input("Enter the user id :")
password=input("Enter the password :")
if userid==correct_userid:
    if password==correct_password:
        print('Loging succesfull')
    else:
        print('Invalid password')
else:
    print('Invalid user ID')