import json
import os

DATA_FILE = "users.json"

def load_users():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_users(users):
    with open(DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)

def add_user(name, email):
    users = load_users()
    users.append({"name": name, "email": email})
    save_users(users)

def view_users():
    users = load_users()
    for user in users:
        print(f"{user['name']} - {user['email']}")

def delete_user(email):
    users = load_users()
    users = [u for u in users if u["email"] != email]
    save_users(users)

if __name__ == "__main__":
    while True:
        print("\n--- User Management System ---")
        print("1. Add User")
        print("2. View Users")
        print("3. Delete User")
        print("4. Exit")
        choice = input("Enter choice (1-4): ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
            print(f"User {name} added.")
        elif choice == "2":
            print("\n--- All Users ---")
            view_users()
        elif choice == "3":
            email = input("Enter email to delete: ")
            delete_user(email)
            print(f"User with email {email} deleted.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")