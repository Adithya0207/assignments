class UserAuth:
    def __init__(self):
        self.users = {"admin": "admin123"}  
    def register(self,username,password):
        if username in self.users:
            return False
        self.users[username] = password
        return True
    
    def login(self,username,password):
        return self.users.get(username) == password
    
    def display_users(self):
        print("Registered Users:")
        print(self.users)
auth=UserAuth()
while True:
        print("1. Register")
        print("2. Login")   
        print("3. Display Users")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if auth.register(username, password):
                print("Registration successful.")
            else:
                print("Username already exists. Please choose a different username.")
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if auth.login(username, password):
                print("Login successful.")
            else:
                print("Invalid username or password.")
        elif choice == "3":
            auth.display_users()
        elif choice == "4":
            print("Exiting...")
            break



