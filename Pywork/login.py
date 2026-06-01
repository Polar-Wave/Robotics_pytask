import getpass

database ={
    "admin" : "password",
    "arman" : "123456"
    }

def main():
    while True:
        print("\nSecure Login System")
        print("===================")
        print("Select an option:")
        print("1 for Registering a new user")
        print("2 for logging in to existing account")
        print("3 for exiting the system")

        choice = int(input("\nEnter your option: "))

        if choice == 1:
            register()
        elif choice == 2:
            login()
        elif choice == 3:
            print("\nClosing the system down, goodbye...")
            break
        else:
            print("Invalid! Enter a number between 1 and 3 only")

def register():
    print("\nNew User Registration")
    print("-" * 25)
    username = input("Enter username: ").strip()

    if username in database:
        print("Username already exists! choose another or login to existing account")
        return
    
    if not username:
        print("Username cannot be empty! Please enter a valid username.")

    password = getpass.getpass("Enter password: ").strip()

    if not password:
        print("Password cannot be empty! Please enter a valid password.")
        return
    
    if len(password) < 6:
        print("Password must be at least 6 characters long! Please choose a stronger password.")
        return
    
    database[username] = password
    print("Registration successful! You can now log in with your new account.")
    
def login():
    print("\nUser Login")
    print("-" * 25)
    username = input("Enter username: ").strip()

    password = getpass.getpass("Enter password: ").strip()

    if username not in database:
        print("Invalid username or password! Please try again.")
        return

    if database[username] == password:
        print("Login successful! Welcome back, {}.".format(username))
    else:
        print("Invalid username or password! Please try again.")

main()