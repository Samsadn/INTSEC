import hashlib
from typing import Optional
import itertools
import string

def hash_salted_password(salt: str, password: str, algorithm: str) -> str:
    """Hash a password with a salt using the specified algorithm."""
    salted = (salt + password).encode()
    
    if algorithm.lower() == 'sha1':
        return hashlib.sha1(salted).hexdigest()
    elif algorithm.lower() == 'md5':
        return hashlib.md5(salted).hexdigest()
    elif algorithm.lower() == 'sha-256' or algorithm.lower() == 'sha256':
        return hashlib.sha256(salted).hexdigest()
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

def try_pin_codes(target_hash: str, salt: str, algorithm: str) -> Optional[str]:
    """Try all possible 4-digit PIN codes."""
    for pin in range(10000):
        pin_str = f"{pin:04d}"
        if hash_salted_password(salt, pin_str, algorithm) == target_hash:
            return pin_str
    return None

def try_literal_passwords(target_hash: str, salt: str, algorithm: str) -> Optional[str]:
    """Try variations of 'literally' and 'password'."""
    base_words = ["password", "literally", "literal"]
    attempts = set()
    
    # Generate variations
    for word in base_words:
        variations = [
            word,
            word.capitalize(),
            word.upper(),
            word.replace('i', '1'),
            word.replace('l', '1'),
            word.replace('e', '3'),
            word.replace('a', '@'),
            word.replace('o', '0'),
            word.replace('s', '5'),
            "L1terally",
            "L1teral",
            "L1t3ral",
            "L1t3rally"
        ]
        attempts.update(variations)
    
    # Try combining variations
    for var in list(attempts):
        attempts.add(var + "password")
        attempts.add("password" + var)
        attempts.add(var + "123")
        attempts.add(var + "!")
    
    # Try specific combinations mentioned in hint
    specific_attempts = [
        "L1terally a password",
        "literally a password",
        "L1t3rally a password",
        "Literally a password",
        "LITERALLY A PASSWORD"
    ]
    attempts.update(specific_attempts)
    
    for attempt in attempts:
        if hash_salted_password(salt, attempt, algorithm) == target_hash:
            return attempt
    
    return None

def try_personal_info(target_hash: str, salt: str, algorithm: str) -> Optional[str]:
    """Try common personal information patterns."""
    # Common personal info patterns
    attempts = [
        "claude",
        "anthropic",
        "assistant",
        "ai",
        "artificial",
        "intelligence",
        "helper",
        "chatbot",
        "language",
        "model",
        "llm"
    ]
    
    # Add variations
    variations = []
    for attempt in attempts:
        variations.extend([
            attempt,
            attempt.capitalize(),
            attempt.upper(),
            attempt + "123",
            attempt + "!",
            attempt.replace('i', '1'),
            attempt.replace('e', '3'),
            attempt.replace('a', '@')
        ])
    
    for attempt in variations:
        if hash_salted_password(salt, attempt, algorithm) == target_hash:
            return attempt
            
    return None

def try_common_passwords(target_hash: str, salt: str, algorithm: str, filename="common_passwords.txt") -> Optional[str]:
    """Try common passwords from a file with password policy variations."""
    try:
        with open(filename, "r") as f:
            for line in f:
                password = line.strip()
                if hash_salted_password(salt, password, algorithm) == target_hash:
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
                    if hash_salted_password(salt, var, algorithm) == target_hash:
                        return var
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    
    return None


def crack_password(algorithm: str, target_hash: str, salt: str, hint: str) -> Optional[str]:
    """Try to crack the password based on the hint."""
    if hint.lower() == "pin code":
        return try_pin_codes(target_hash, salt, algorithm)
    elif "l1tera11y" in hint.lower() or "password" in hint.lower():
        return try_literal_passwords(target_hash, salt, algorithm)
    elif "HT2024" in hint.lower() and "harrand" in hint.lower():
        return try_personal_info(target_hash, salt, algorithm)
    
    # If hint-based approach fails, try all methods including common passwords
    methods = [try_pin_codes, try_literal_passwords, try_personal_info, try_common_passwords]
    for method in methods:
        result = method(target_hash, salt, algorithm)
        if result:
            return result
    
    return None

def main():
    hashes = [
        ("SHA1", "57536215cfe9781d21733fcab27a653e9db92577", "1fa6", "PIN code"),
        ("SHA-256", "8421f0e3432bb339f3671341bc1ec96f6eb283dbf65bb56793065458c20cf945", "cb63", "L1tera11y a password"),
        ("md5", "e75a0b86d4f30e2e56a73cbe9d7dbf07", "e098", "You need to know something (obvious) about me.")
    ]
    
    print("Educational Salted Password Cracker - Demonstrating Why Strong Passwords Matter\n")
    
    for algorithm, hash_value, salt, hint in hashes:
        print(f"Attempting to crack hash: {hash_value}")
        print(f"Algorithm: {algorithm}")
        print(f"Salt: {salt}")
        print(f"Hint: {hint}")
        
        result = crack_password(algorithm, hash_value, salt, hint)
        
        if result:
            print(f"Password found: {result}")
        else:
            print("Password not found")
        print("-" * 50 + "\n")

if __name__ == "__main__":
    main()