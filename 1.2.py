from itertools import cycle
import string

def xor_bytes(data: bytes, key: bytes) -> bytes:
    """XOR data with a repeating key."""
    return bytes(a ^ b for a, b in zip(data, cycle(key)))

def is_printable_ascii(text: bytes) -> bool:
    """Check if decrypted text is valid printable ASCII."""
    try:
        decoded = text.decode('ascii')
        return all(c in string.printable for c in decoded)
    except:
        return False

def get_possible_keys(encrypted_data: bytes, known_prefix: bytes, key_length: int = 15) -> list:
    """Generate possible keys based on known plaintext prefix."""
    # Get the initial part of the key from known prefix
    initial_key = bytes(a ^ b for a, b in zip(encrypted_data[:len(known_prefix)], known_prefix))
    
    # Pad or truncate to exact key length
    if len(initial_key) < key_length:
        # Try different padding options
        possible_keys = []
        # Try padding with common characters
        for pad_char in b'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            padded_key = initial_key + bytes([pad_char] * (key_length - len(initial_key)))
            possible_keys.append(padded_key)
        return possible_keys
    else:
        return [initial_key[:key_length]]

def try_decrypt_file(filename: str):
    """Attempt to decrypt the file with various key possibilities."""
    # Read encrypted data
    with open(filename, 'rb') as f:
        encrypted_data = f.read()
    
    known_prefix = b"Challenge 1.2"
    possible_keys = get_possible_keys(encrypted_data, known_prefix)
    
    best_decryption = None
    best_key = None
    best_printable_ratio = 0
    
    for key in possible_keys:
        decrypted = xor_bytes(encrypted_data, key)
        
        if decrypted.startswith(known_prefix):
            # Calculate ratio of printable characters
            try:
                decoded = decrypted.decode('ascii')
                printable_ratio = sum(c in string.printable for c in decoded) / len(decoded)
                
                if printable_ratio > best_printable_ratio:
                    best_printable_ratio = printable_ratio
                    best_decryption = decrypted
                    best_key = key
            except:
                continue
    
    if best_decryption:
        print("Successfully decrypted!")
        print("\nDecrypted text:")
        try:
            print(best_decryption.decode('ascii'))
        except UnicodeDecodeError:
            print("Warning: Could not decode as ASCII. Showing raw bytes:")
            print(best_decryption)
        
        print("\nKey (hex):", best_key.hex())
        print("Key (bytes):", best_key)
        print(f"Printable character ratio: {best_printable_ratio:.2%}")
        
        # Save the decrypted content
        with open('decrypted_output.txt', 'wb') as f:
            f.write(best_decryption)
    else:
        print("Could not find a valid decryption.")

if __name__ == "__main__":
    try:
        try_decrypt_file('Challenge-1.2.enc')
    except FileNotFoundError:
        print("Error: Could not find the encrypted file.")
    except Exception as e:
        print(f"Error occurred: {e}")