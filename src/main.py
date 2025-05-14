import base64
import argparse

def encode_base64(text):
    """Encode text to Base64"""
    if isinstance(text, str):
        text = text.encode('utf-8')
    encoded = base64.b64encode(text)
    return encoded.decode('utf-8')

def decode_base64(encoded_text):
    """Decode Base64 to text"""
    try:
        decoded = base64.b64decode(encoded_text)
        return decoded.decode('utf-8')
    except Exception as e:
        return f"Error decoding: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description='Encode or decode Base64')
    parser.add_argument('action', choices=['encode', 'decode'], help='Action to perform')
    parser.add_argument('text', help='Text to process')
    parser.add_argument('-f', '--file', help='Input from file instead of text argument')
    
    args = parser.parse_args()
    
    # Get input from file or command line
    if args.file:
        try:
            with open(args.file, 'r') as file:
                input_text = file.read()
        except Exception as e:
            print(f"Error reading file: {e}")
            return
    else:
        input_text = args.text
    
    # Perform the requested action
    if args.action == 'encode':
        result = encode_base64(input_text)
        print(f"Encoded: {result}")
    else:
        result = decode_base64(input_text)
        print(f"Decoded: {result}")

if __name__ == "__main__":
    main()