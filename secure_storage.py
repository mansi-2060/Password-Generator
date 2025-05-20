from cryptography.fernet import Fernet
import json
import os


KEY_FILE = "key.key"
PASSWORD_FILE = "passwords.json"

def generate_key():
    """Generate a new encryption key and save it to a file."""
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

def load_key():
    """Load the encryption key from a file."""
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

def encrypt_password(password):
    """Encrypt a password using the loaded key."""
    key = load_key()
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    """Decrypt a password using the loaded key."""
    key = load_key()
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(encrypted_password.encode()).decode()

def save_password(website, password):
    """Save an encrypted password to a JSON file."""
    encrypted_password = encrypt_password(password)
    data = {website: encrypted_password}

    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = {}
    else:
        existing_data = {}

    existing_data.update(data)

    with open(PASSWORD_FILE, "w") as file:
        json.dump(existing_data, file, indent=4)

def load_passwords():
    """Load and decrypt stored passwords."""
    if not os.path.exists(PASSWORD_FILE):
        return {}

    with open(PASSWORD_FILE, "r") as file:
        try:
            encrypted_data = json.load(file)
        except json.JSONDecodeError:
            return {}

    decrypted_data = {website: decrypt_password(enc_password) for website, enc_password in encrypted_data.items()}
    return decrypted_data
