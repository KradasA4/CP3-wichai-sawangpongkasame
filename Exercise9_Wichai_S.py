username = 0
password = 0
while username != "admin" or password != "1234":
    username = input("enter username: ")
    password = input("enter password: ")
    if username!="admin" or password!="1234":
        print ("Incorrect username or password, access denied.")
    else:
        print ("correct!")
