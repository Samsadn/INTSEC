import hashlib
import itertools
import string

def crack_hash(hash_to_crack, hash_function):
    characters = string.ascii_lowercase + string.digits
    for length in range(1, 10):  # Try passwords up to length 9
        for attempt in itertools.product(characters, repeat=length):
            password = ''.join(attempt)
            if hash_function(password.encode()).hexdigest() == hash_to_crack:
                return password
    return None

# Test the cracking functions
md5_hash = "c49078e81caafab96c08390197cf6a96"
sha256_hash = "b81848b9e4857c5ed8da601fa6ba92d9c2ee6c6aceabcf5e09813b427dab7bfc"

print(f"MD5: {crack_hash(md5_hash, hashlib.md5)}")
print(f"SHA-256: {crack_hash(sha256_hash, hashlib.sha256)}")
