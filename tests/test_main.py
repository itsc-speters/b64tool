import unittest
import os
from b64tool import encode_base64, decode_base64

class TestBase64Functions(unittest.TestCase):

    def test_encode_decode_text(self):
        """Test that encoding and then decoding produces the original text"""
        original_text = "Hello, World!"
        encoded = encode_base64(original_text)
        decoded = decode_base64(encoded)
        self.assertEqual(decoded, original_text)
    
    def test_encode_text(self):
        """Test encoding specific text to known Base64 value"""
        test_cases = [
            ("Hello, World!", "SGVsbG8sIFdvcmxkIQ=="),
            ("Python is awesome", "UHl0aG9uIGlzIGF3ZXNvbWU="),
            ("", "")
        ]
        for text, expected in test_cases:
            with self.subTest(text=text):
                self.assertEqual(encode_base64(text), expected)
    
    def test_decode_text(self):
        """Test decoding specific Base64 values to known text"""
        test_cases = [
            ("SGVsbG8sIFdvcmxkIQ==", "Hello, World!"),
            ("UHl0aG9uIGlzIGF3ZXNvbWU=", "Python is awesome"),
            ("", "")
        ]
        for encoded, expected in test_cases:
            with self.subTest(encoded=encoded):
                self.assertEqual(decode_base64(encoded), expected)
    
    def test_decode_invalid(self):
        """Test decoding invalid Base64 values"""
        # Should return an error message, not crash
        result = decode_base64("This is not valid Base64!")
        self.assertTrue(result.startswith("Error decoding:"))

    def test_file_output(self):
        """Test encoding and decoding with file output"""
        test_string = "Test string for file output"
        test_file = "test_output.txt"
        
        # Clean up any existing test file
        if os.path.exists(test_file):
            os.remove(test_file)
            
        # Encode to file and verify
        encoded = encode_base64(test_string)
        with open(test_file, "w") as f:
            f.write(encoded)
            
        with open(test_file, "r") as f:
            read_encoded = f.read()
            
        self.assertEqual(read_encoded, encoded)
        
        # Decode from file and verify
        decoded = decode_base64(read_encoded)
        self.assertEqual(decoded, test_string)
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)

if __name__ == "__main__":
    unittest.main()