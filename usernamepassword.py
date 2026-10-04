username = (input("Enter Username"))
password = (input("Enter Password"))

if username == "Admin" and password == "76767676":
    print("Access Granted")
elif username != "Admin":
    print("Username Is Incorrect")
elif password != "76767676":
    print("Password is Incorrect")
else:
    print("Access Not Granted")

