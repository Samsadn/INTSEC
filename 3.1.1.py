import hashlib
import itertools
import string

def crack_sha1(hash_to_crack):
    for i in range(10000):  # All 4-digit PIN codes
        pin = f"{i:04d}"
        if hashlib.sha1(pin.encode()).hexdigest() == hash_to_crack:
            return pin
    return None

def crack_md5(hash_to_crack):
    keyboard_rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    for length in range(1, 11):  # Try lengths up to 10
        for row in keyboard_rows:
            for password in itertools.combinations_with_replacement(row, length):
                password = ''.join(password)
                if hashlib.md5(password.encode()).hexdigest() == hash_to_crack:
                    return password
    return None

def crack_sha256(hash_to_crack):
    common_words = ["password", "letmein", "welcome", "admin"]
    digits = string.digits
    for word in common_words:
        for length in range(1, 5):  # Try adding up to 4 digits
            for suffix in itertools.product(digits, repeat=length):
                password = word + ''.join(suffix)
                if hashlib.sha256(password.encode()).hexdigest() == hash_to_crack:
                    return password
    return None

# Test the cracking functions
sha1_hash = "30139264c3ec85759ce4f83c2fe286ecb63e6d43"
md5_hash = "c49078e81caafab96c08390197cf6a96"
sha256_hash = "b81848b9e4857c5ed8da601fa6ba92d9c2ee6c6aceabcf5e09813b427dab7bfc"

print(f"SHA1 (PIN code): {crack_sha1(sha1_hash)}")
print(f"MD5 (keyboard-based): {crack_md5(md5_hash)}")
print(f"SHA-256 (common password): {crack_sha256(sha256_hash)}")
