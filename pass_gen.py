import random
import json
import os
import string

# The file where passwords will be saved locally
FILE_NAME = "passwords.json"

def load_passwords():
    """Reads the JSON file and returns the stored passwords."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

def save_password(service, password):
    """Saves a new service and password to the JSON file."""
    passwords = load_passwords()
    passwords[service] = password
    with open(FILE_NAME, "w") as file:
        json.dump(passwords, file, indent=4)

def generate_password():
    # Using the built-in string module guarantees all letters, numbers, and symbols are included
    characters = string.ascii_letters + string.digits + string.punctuation
    
    service = input("\nWhat service is this password for? (e.g., Gmail, Bank): ")
    pass_length = int(input("Enter the length of password: "))

    password = ""
    for i in range(pass_length):
        password += random.choice(characters)

    print(f"\nYour generated password for {service} is: {password}")
    
    # Save it to local storage
    save_password(service, password)
    print(f"✅ Password for {service} saved successfully!")

def retrieve_password():
    passwords = load_passwords()
    
    if not passwords:
        print("\n❌ No passwords saved yet!")
        return

    print("\nSaved Services:")
    for service in passwords.keys():
        print(f"- {service}")
        
    service_to_find = input("\nEnter the service name to retrieve its password: ")
    
    if service_to_find in passwords:
        print(f"\n🔑 Password for {service_to_find}: {passwords[service_to_find]}")
    else:
        print(f"\n❌ No password found for '{service_to_find}'.")

def main():
    print("+" * 31)
    print("Welcome to Password Manager!")
    print("+" * 31)
    
    while True:
        print("\nOptions:")
        print("1. Generate and save a new password")
        print("2. Retrieve a saved password")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            generate_password()
        elif choice == '2':
            retrieve_password()
        elif choice == '3':
            print("\nTata!")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()