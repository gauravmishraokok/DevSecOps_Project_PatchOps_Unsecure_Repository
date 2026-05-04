import re

def is_valid_username(username):
    return len(username) >= 3 and re.match(r'^\w+$', username)

def is_strong_password(password):
    return len(password) >= 8 and any(c.isdigit() for c in password)
