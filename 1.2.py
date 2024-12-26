from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend

def try_decrypt(encrypted_content, key, debug=False):
    """
    Attempt to decrypt the content with a given key
    Returns the decrypted text if successful, None if failed
    """
    try:
        iv = encrypted_content[:16]
        ciphertext = encrypted_content[16:]
        
        # Add padding to make ciphertext length multiple of 16
        remainder = len(ciphertext) % 16
        if remainder != 0:
            padding_length = 16 - remainder
            ciphertext = ciphertext + (b'\x00' * padding_length)
        
        if debug:
            print(f"Key length: {len(key)} bytes")
            print(f"Key (hex): {key.hex()}")
            print(f"Key (ascii): {key.decode('ascii', errors='replace')}")
        
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
        
        try:
            unpadder = PKCS7(algorithms.AES.block_size).unpadder()
            decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()
        except ValueError:
            decrypted = decrypted_padded
        
        try:
            decoded = decrypted.decode('ascii', errors='replace')
            if "Challenge 1.2" in decoded[:20]:
                return decoded
            elif debug:
                print(f"Decrypted start: {decoded[:50]}")
        except UnicodeDecodeError:
            if debug:
                print("Failed to decode as ASCII")
        return None
    except Exception as e:
        if debug:
            print(f"Decryption error: {e}")
        return None

# Read the encrypted file
file_path = "C:/Users/frog2/IOT/INTSEC/Challenge-1.2.enc"

with open(file_path, "rb") as file:
    encrypted_content = file.read()

def try_keys():
    # Try variations of Challenge1.2 to reach exactly 15 bytes
    base_patterns = [
        "Challenge1dot2",    # 13 bytes
        "Challenge1.2xxx",   # Fill with x
        "Challenge1.2key",   # Common pattern
        "Challenge1.2CTF",   # CTF style
        "Challenge1.2IOT",   # Course related
        "Challenge1.2INT",   # Course related
        "Challenge12KEY15",  # Another format
        "Chall1.2Crypto1",  # Crypto reference
        "Challenge1.2SEC"    # Security reference
    ]
    
    for pattern in base_patterns:
        # Ensure pattern is exactly 15 bytes
        if len(pattern) > 15:
            pattern = pattern[:15]
        elif len(pattern) < 15:
            pattern = pattern + 'X' * (15 - len(pattern))
            
        key = pattern.encode('ascii') + b'\x00'  # Add null byte for 16-byte AES key
        
        print(f"\nTrying key: {pattern}")
        result = try_decrypt(encrypted_content, key, debug=True)
        if result:
            print("\nSuccess! Found working key!")
            print("\nDecrypted text:")
            print(result)
            return True
    
    return False

# Run the key testing
if not try_keys():
    print("\nCould not find the correct key.")
    print("Should we try:")
    print("1. Different variations of Challenge1.2?")
    print("2. Different padding characters?")
    print("3. All uppercase/lowercase variations?")