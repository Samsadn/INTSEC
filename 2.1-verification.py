import hashlib
import struct

def sha1_pad(msg):
    """Pads a message for SHA-1 as per RFC 3174."""
    ml = len(msg) * 8  # message length in bits
    msg += b"\x80"  # append the "1" bit followed by 7 0 bits
    msg += b"\x00" * ((56 - (len(msg) % 64)) % 64)  # pad with zeros until 56 bytes mod 64
    msg += ml.to_bytes(8, byteorder="big")  # append the message length in bits as a 64-bit big-endian integer
    return msg

def insecure_hmac(key, message):
    """Simulates the insecure HMAC using SHA-1: h(key | message)"""
    return hashlib.sha1(key + message).hexdigest().upper()

key = b'\x00' * 7  # Simulate a 7-byte key (value unknown)
original_message = b"I give you the following amount of SEK coded in binary:\x12"
extension = b"\x00"  # Example extension
padded_message = sha1_pad(key + original_message)[7:]  # Remove key padding
new_message = padded_message + extension

# Compute the insecure HMAC for verification
computed_hmac = insecure_hmac(key, new_message)
print(f"Computed HMAC: {computed_hmac}")
print(f"Your HMAC:     5BA93C9DB0CFF93F52B521D7420E43F6EDA2784F")
