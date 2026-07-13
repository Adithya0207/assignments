username = "admin"
password = "1234"
attempts = 3
while attempts > 0:
    user = input("Enter Username: ")
    pwd = input("Enter Password: ")
    if user == username and pwd == password:
        print("Login Successful")
        break
    else:
        attempts -= 1
        print("Invalid Password")
        print(attempts, "attempts left")
if attempts == 0:
    print("Account Blocked")
