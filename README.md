# Encoder
Encodes txt file lines
    Encode text files with four different encoding types.
    Apply multiple encoding steps in sequence (e.g., URL encoding followed by Base64 encoding).
    Output files are named according to the encoding types applied for easy identification.

Available Encoding Types

1. URL Encoding: Encodes text to be safely included in URLs.
2. HTML Entity Encoding: Converts characters to their HTML entity representations.
3. Hexadecimal Encoding: Encodes text to its hexadecimal form.
4. Base64 Encoding: Encodes text in Base64 format.

## Usage

Clone the repository:


    git clone https://github.com/your-username/Encoder.git
    cd Encoder

Run the script:

    python encoder.py

Input Instructions:
        Enter the name of the text file you wish to encode when prompted.
        Choose the encoding options by entering a sequence of numbers separated by commas (e.g., 1,1,2 for applying URL encoding twice followed by HTML entity encoding).

Output:
        The script outputs an encoded file named with the types of encodings applied, e.g., encoded_URL_URL_HTML_input.txt.

## Example

![image](https://github.com/user-attachments/assets/3c53a09c-9983-4703-b2b8-2bc709aec13f)


Input:


Enter the name of the text file: input.txt
Enter your choices separated by commas (e.g., 1,2,3): 1,4

Output: The file encoded_URL_Base64_input.txt will be created containing the encoded text.
Requirements

    Python 3.x
    Standard Python libraries (urllib, base64)
