import hashlib
from typing import Optional
import itertools
import string

def hash_password(password: str, algorithm: str) -> str:
    """Hash a password using the specified algorithm."""
    if algorithm.lower() == 'sha1':
        return hashlib.sha1(password.encode()).hexdigest()
    elif algorithm.lower() == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm.lower() == 'sha-256' or algorithm.lower() == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

def try_pin_codes(target_hash: str, algorithm: str) -> Optional[str]:
    """Try all possible 4-digit PIN codes."""
    for pin in range(10000):
        pin_str = f"{pin:04d}"
        if hash_password(pin_str, algorithm) == target_hash:
            return pin_str
    return None

def try_keyboard_variations(target_hash: str, algorithm: str) -> Optional[str]:
    """Try extensive keyboard and key-related patterns."""
    # Basic key-related words
    base_words = ["key", "keys", "keyboard"]
    
    # Generate variations
    attempts = set()
    for word in base_words:
        # Basic variations
        variations = [
            word,
            word.upper(),
            word.capitalize(),
            # Reverse
            word[::-1],
            # Common numbers
            word + "123",
            word + "1234",
            word + "12",
            "123" + word,
            # Single keys
            "k3y",
            "k3ys",
            # Multiple keys
            "k3yk3y",
            # Special characters
            word + "!",
            word + "@",
            word + "#",
            "!" + word
        ]
        attempts.update(variations)
        # Add numbered variations
        for i in range(10):
            attempts.add(f"key{i}")
    
    # Function keys patterns
    for i in range(1, 13):
        attempts.add(f"f{i}")
        attempts.add(f"F{i}")
        attempts.add(f"function{i}")
        attempts.add(f"functionkey{i}")
        
    # Try keyboard rows
    keyboard_rows = [
        "1234567890",
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm"
    ]
    
    # Add keyboard patterns
    for row in keyboard_rows:
        for length in range(2, len(row) + 1):
            for i in range(len(row) - length + 1):
                pattern = row[i:i + length]
                attempts.add(pattern)
                attempts.add(pattern.upper())
    
    # Try all generated attempts
    for attempt in attempts:
        if hash_password(attempt, algorithm) == target_hash:
            return attempt
            
    return None

def try_common_passwords(target_hash: str, algorithm: str, filename="common_passwords.txt") -> Optional[str]:
    """Try common passwords from a file with password policy variations."""
    try:
        with open(filename, "r") as f:
            for line in f:
                password = line.strip()
                if hash_password(password, algorithm) == target_hash:
                    return password

                # Try variations with different cases and common substitutions
                variations = [
                    password.upper(),
                    password.capitalize(),
                    password.replace('e', '3'),
                    password.replace('a', '@'),
                    password.replace('i', '1'),
                    password.replace('o', '0'),
                    password.replace('s', '$'),
                    password + "!",
                    password + "@",
                    password + "#",
                    password + "$",
                    "!" + password,
                    "@" + password
                ]

                for var in variations:
                    if hash_password(var, algorithm) == target_hash:
                        return var
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    
    return None

def crack_password(algorithm: str, target_hash: str, hint: str) -> Optional[str]:
    """Try to crack the password based on the hint."""
    if hint.lower() == "pin code":
        return try_pin_codes(target_hash, algorithm)
    elif "key" in hint.lower():
        result = try_keyboard_variations(target_hash, algorithm)
        if result:
            return result
    
    # Try common passwords as fallback
    return try_common_passwords(target_hash, algorithm)

def main():
    hashes = [
        ("SHA1", "30139264c3ec85759ce4f83c2fe286ecb63e6d43", "PIN code"),
        ("md5", "c49078e81caafab96c08390197cf6a96", "you need to find the right key(s)"),
        ("SHA-256", "b81848b9e4857c5ed8da601fa6ba92d9c2ee6c6aceabcf5e09813b427dab7bfc", "Common password")
    ]
    
    print("Educational Password Cracker - Demonstrating Why Strong Passwords Matter\n")
    
    for algorithm, hash_value, hint in hashes:
        print(f"Attempting to crack hash: {hash_value}")
        print(f"Algorithm: {algorithm}")
        print(f"Hint: {hint}")
        
        result = crack_password(algorithm, hash_value, hint)
        
        if result:
            print(f"Password found: {result}")
        else:
            print("Password not found")
        print("-" * 50 + "\n")

if __name__ == "__main__":
    main()