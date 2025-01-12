import unittest

def xor_cipher(ciphertext, key):
    """Encrypts/decrypts data using XOR with a key.

    Args:
        ciphertext (bytes): The data to be encrypted or decrypted.
        key (bytes): The key to use for XOR operation.

    Returns:
        bytes: The encrypted or decrypted data.
    """
    extended_key = key * (len(ciphertext) // len(key) + 1)
    return bytes([a ^ b for a, b in zip(ciphertext, extended_key)])

class TestXORCipher(unittest.TestCase):
    # Initialization
    def setUp(self):
        """Setup method to prepare test data."""
        self.key = b"secret_key"
        self.plaintext = b"This is a test string with various characters: !@#$%^&*()_+=-`~[]\{}|;':\",./<>?"

    # Function under test
    def test_encryption_decryption(self):
        """Tests if encryption followed by decryption results in the original plaintext."""
        ciphertext = xor_cipher(self.plaintext, self.key)
        decrypted_text = xor_cipher(ciphertext, self.key)
        # Oracle
        self.assertEqual(decrypted_text, self.plaintext)

    def test_empty_input(self):
        """Tests the behavior with empty input."""
        empty_text = b""
        ciphertext = xor_cipher(empty_text, self.key)
        decrypted_text = xor_cipher(ciphertext, self.key)
        # Oracle
        self.assertEqual(decrypted_text, empty_text)

    def test_different_key_lengths(self):
        """Tests with keys of different lengths."""
        for key_length in range(1, 16):
            test_key = b"k" * key_length
            ciphertext = xor_cipher(self.plaintext, test_key)
            decrypted_text = xor_cipher(ciphertext, test_key)
            # Oracle
            self.assertEqual(decrypted_text, self.plaintext)

if __name__ == '__main__':
    unittest.main()