# Password Manager & Generator

A simple, command-line Python application that generates secure, random passwords and stores them locally for easy retrieval. 

## Features
- **Generate Secure Passwords:** Creates strong passwords using a mix of uppercase letters, lowercase letters, numbers, and symbols.
- **Customizable Length:** You decide exactly how long you want your password to be.
- **Local Storage:** Automatically saves your generated passwords to a local `passwords.json` file so you never lose them.
- **Easy Retrieval:** Look up your saved passwords by the service name (e.g., "Netflix", "Gmail").
- **Interactive Menu:** Simple text-based interface to navigate between generating and retrieving passwords.

## Prerequisites
- Python 3.x installed on your machine.
- No external libraries are required! The script uses only Python's built-in modules (`random`, `json`, `os`, `string`).

## How to Run
1. Save the Python script as `password_manager.py`.
2. Open your terminal or command prompt.
3. Navigate to the folder where you saved the script.
4. Run the following command:
   ```bash
   python password_manager.py
   ```

## Usage
When you start the script, you will be greeted with a menu:
```text
+++++++++++++++++++++++++++++++
Welcome to Password Manager!
+++++++++++++++++++++++++++++++

Options:
1. Generate and save a new password
2. Retrieve a saved password
3. Exit
```
Simply type `1`, `2`, or `3` and press **Enter** to navigate the app.

## ⚠️ Security Note
This project is an excellent way to learn Python, file handling, and JSON. However, it stores passwords in **plain text** inside the `passwords.json` file. 

For real-world, high-security accounts (like your bank or primary email), it is highly recommended to use an encrypted password manager (like Bitwarden or 1Password) or to learn how to add an encryption module (like `cryptography`) to this script in the future!
