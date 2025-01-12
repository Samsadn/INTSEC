import struct
import hashlib

def sha1_padding(message_len):
    """Generate SHA-1 padding for a given message length."""
    padding = b'\x80'  # Start with 0x80
    padding_len = (56 - (message_len + 1) % 64) % 64  # Padding to make total length % 64 = 56
    padding += b'\x00' * padding_len
    padding += struct.pack('>Q', message_len * 8)  # Append original message length in bits
    return padding

def length_extension_attack(hmac_value, original_msg, append_data, key_length):
    """Perform a SHA-1 length extension attack."""
    
    # Parse the given HMAC into SHA-1 internal state (5 x 32-bit words)
    hmac_words = struct.unpack('>5I', hmac_value)
    
    # Compute padding for the original message + key
    original_len = key_length + len(original_msg)
    padding = sha1_padding(original_len)
    
    # Compute the new total length (with padding and additional data)
    new_len = original_len + len(padding) + len(append_data)
    
    # Simulate SHA-1 hashing starting from the given internal state
    sha1 = hashlib.sha1()
    sha1._h = hmac_words  # Set the internal state (unofficial API usage)
    sha1.update(append_data)  # Hash the additional data
    
    # Get the new HMAC value
    new_hmac = sha1.digest()
    
    # Construct the extended message: original message + padding + new data
    extended_message = original_msg.encode() + padding + append_data
    
    return extended_message, new_hmac

# Given values
original_message = "I give you the following amount of SEK coded in binary:\x12"
hmac_value = bytes.fromhex("67452301EFCDAB8998BADCFE10325476C3D2E1F0")
key_length = 7  # 7 bytes key length
additional_data = b"20"  # This is the new number (in binary encoded as ascii)

# Perform the length extension attack
extended_message, extended_hmac = length_extension_attack(hmac_value, original_message, additional_data, key_length)

# Print the results
print("Extended Message:", extended_message.decode(errors='ignore'))
print("Extended HMAC (hex):", extended_hmac.hex())
