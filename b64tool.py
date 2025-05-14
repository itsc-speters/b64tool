#!/usr/bin/env python
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
    parser.add_argument('text', nargs='?', help='Text to process')
    parser.add_argument('-f', '--file', help='Input from file instead of text argument')
    parser.add_argument('-o', '--output', help='Output file to save the result')
    
    args = parser.parse_args()
    
    # Get input from file or command line
    if args.file:
        try:
            with open(args.file, 'r') as file:
                input_text = file.read()
        except Exception as e:
            print(f"Error reading file: {e}")
            return
    elif args.text:
        input_text = args.text
    else:
        parser.error("Either text argument or --file option is required")
    
    # Perform the requested action
    if args.action == 'encode':
        result = encode_base64(input_text)
        output_prefix = "Encoded"
    else:
        result = decode_base64(input_text)
        output_prefix = "Decoded"
    
    # Handle output - either to file or console
    if args.output:
        try:
            with open(args.output, 'w') as file:
                file.write(result)
            print(f"{output_prefix} result saved to {args.output}")
        except Exception as e:
            print(f"Error writing to file: {e}")
    else:
        print(f"{output_prefix}: {result}")

if __name__ == "__main__":
    main()
