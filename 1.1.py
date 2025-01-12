def caesar_cipher(text, key, mode='decrypt'):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890"
    result = ''
    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            if mode == 'decrypt':
                new_index = (char_index - key) % len(alphabet)
            else:
                new_index = (char_index + key) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += char
    return result

def frequency_score(text):
    """Calculate a score based on English letter frequency."""
    english_freq = {
        'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97,
        'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25,
        'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36,
        'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.49,
        'V': 0.98, 'K': 0.77, 'X': 0.15, 'J': 0.15, 'Q': 0.10, 'Z': 0.07
    }
    
    score = 0
    for char in text.upper():
        if char in english_freq:
            score += english_freq[char]
    return score

# Provided ciphertext
ciphertext = """D_AZ_5H7S006_9WHF6BHD_33HX_5
VHSAH3WS0AHIJHX3SY0H064WH6XH
AZW4HS9WHX_3WH5S4WVHX3SYH5HT
BAH064WA_4W0HAZWHX3SYH_0HZ_V
VW5H_5HS56AZW9HX_3WHAZ_0H4W0
0SYWH_0HAZWHS50DW9HA6HUZS33W
5YWHIHV6AHI"""

# Brute-force attack with frequency analysis
best_key = None
best_score = 0
best_decryption = ""

for key in range(1, 37):
    decrypted_text = caesar_cipher(ciphertext, key)
    score = frequency_score(decrypted_text)
    print(f"Key {key}: {decrypted_text} (Score: {score})")
    
    if score > best_score:
        best_score = score
        best_key = key
        best_decryption = decrypted_text

print("\nMost likely key:", best_key)
print("Decrypted text:", best_decryption)
