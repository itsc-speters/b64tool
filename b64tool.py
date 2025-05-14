#!/usr/bin/env python
"""
b64tool - A command line utility for encoding and decoding Base64.

This module provides functions to encode text to Base64 and decode Base64 back to text,
along with a command-line interface to use these functions.
"""

import base64
import argparse
import sys
from typing import Union

def encode_base64(text: Union[str, bytes]) -> str:
    """
    Encode text to Base64.

    Args:
        text: The text to encode (string or bytes)

    Returns:
        The Base64 encoded string
    """
    if isinstance(text, str):
        text = text.encode('utf-8')
    encoded = base64.b64encode(text)
    return encoded.decode('utf-8')

def decode_base64(encoded_text: str) -> str:
    """
    Decode Base64 to text.

    Args:
        encoded_text: The Base64 encoded string

    Returns:
        The decoded text or an error message
    """
    try:
        decoded = base64.b64decode(encoded_text)
        return decoded.decode('utf-8')
    except (base64.binascii.Error, UnicodeDecodeError) as err:
        return f"Error decoding: {str(err)}"

def main() -> None:
    """
    Process command line arguments and execute the requested Base64 operation.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(description='Encode or decode Base64')
    parser.add_argument('action', choices=['encode', 'e', 'decode', 'd'], 
                        help='Action to perform (encode/e or decode/d)')
    parser.add_argument('text', nargs='?', help='Text to process')
    parser.add_argument('-f', '--file', help='Input from file instead of text argument')
    parser.add_argument('-o', '--output', help='Output file to save the result')

    args = parser.parse_args()

    # Initialize input_text to None to avoid possibly-used-before-assignment issue
    input_text = None

    # Get input from file or command line
    if args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as file:
                input_text = file.read()
        except IOError as err:
            print(f"Error reading file: {err}")
            sys.exit(1)
    elif args.text:
        input_text = args.text
    else:
        parser.error("Either text argument or --file option is required")

    # Perform the requested action
    if args.action in ('encode', 'e'):
        result = encode_base64(input_text)
        output_prefix = "Encoded"
    else:  # 'decode' or 'd'
        result = decode_base64(input_text)
        output_prefix = "Decoded"

    # Handle output - either to file or console
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as file:
                file.write(result)
            print(f"{output_prefix} result saved to {args.output}")
        except IOError as err:
            print(f"Error writing to file: {err}")
            sys.exit(1)
    else:
        print(f"{output_prefix}: {result}")

if __name__ == "__main__":
    main()
