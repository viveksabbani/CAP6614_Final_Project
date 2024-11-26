# Vulnerable code using weak cryptographic algorithm (MD5)

import hashlib

def store_password(username, password):
    # Storing password hash using MD5 (weak hash function)
    password_hash = hashlib.md5(password.encode()).hexdigest()
    # Save username and password_hash to the database (simulated here)
    print(f"Storing {username}'s password hash: {password_hash}")

# Usage
store_password('user1', 'password123')