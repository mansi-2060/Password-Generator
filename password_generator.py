import random
import string

def generate_password(length=12, use_special_chars=True):
    """
    Function to generate a random password
    :param length: Length of the password (default is 12)
    :param use_special_chars: If True, includes special characters (default is True)
    :return: A generated password string
    """
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
