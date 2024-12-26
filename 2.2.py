import hashlib

def calculate_hmac(key1, key2, message):
    # Inner hash
    inner_hash = hashlib.sha1((key1 + message).encode('ascii')).hexdigest()
    
    # Outer hash
    outer_hash = hashlib.sha1((key2 + inner_hash).encode('ascii')).hexdigest()
    
    return outer_hash

# Keys
key1 = "1234"
key2 = "5678"

# Messages and their provided HMACs
messages = [
    ("Challenge 2.2 is easy.", "12d44a1c2448cc54ddffc75e69313a7964d5d775"),
    ("Challenge 2.2 is doable.", "1b25d0e281f73935f7a122c088c1bc34686b271b"),
    ("Challenge 2.2 is hard.", "aec64e480f251c6811686597305b04edcc25da35")
]

# Verify each message
for message, provided_hmac in messages:
    calculated_hmac = calculate_hmac(key1, key2, message)
    is_valid = calculated_hmac == provided_hmac
    print(f"Message: {message}")
    print(f"Calculated HMAC: {calculated_hmac}")
    print(f"Provided HMAC: {provided_hmac}")
    print(f"Valid: {is_valid}\n")
