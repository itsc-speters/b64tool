# b64tool - Base64 Encoder/Decoder

## Overview

This project provides a command-line tool to encode text to Base64 format and decode Base64 text back to plain text. It handles both direct command-line input and file-based input.

## Installation

### Option 1: Install as Python module

Clone the repository and install:

```bash
# For users (standard installation)
pip install .

# For developers (editable installation)
# Changes to the code will be immediately available without reinstalling
pip install -e .
```

### Option 2: Run directly

This project uses only Python standard libraries, so no external dependencies are required.

```bash
# Make the script executable
chmod +x b64tool.py
```

## Usage

### If installed with pip

```bash
# To encode text
b64tool encode "Hello World"

# To decode Base64
b64tool decode "SGVsbG8gV29ybGQ="

# To encode from a file
b64tool encode -f input.txt

# To decode from a file
b64tool decode -f encoded.txt

# To save output to a file
b64tool encode "Hello World" -o encoded.txt
b64tool decode -f encoded.txt -o decoded.txt
```

Alternatively, you can also run it as a Python module:

```bash
python -m b64tool [options]
```

### If running directly

```bash
# To encode text
./b64tool.py encode "Hello World"

# To decode Base64
./b64tool.py decode "SGVsbG8gV29ybGQ="

# To encode from a file
./b64tool.py encode -f input.txt

# To decode from a file
./b64tool.py decode -f encoded.txt

# To save output to a file
./b64tool.py encode "Hello World" -o encoded.txt
./b64tool.py decode -f encoded.txt -o decoded.txt
```

## Running Tests

To run the unit tests, use the following command:

```bash
python -m unittest discover -s tests
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License.
