import urllib.parse
import base64

def encode_to_url(text):
    return urllib.parse.quote(text)

def encode_to_html_entity(text):
    return ''.join(['&#{:d};'.format(ord(char)) for char in text])

def encode_to_hex(text):
    return ''.join([hex(ord(char))[2:] for char in text])

def encode_to_base64(text):
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')

def main():
    file_name = input("Enter the name of the text file: ")
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return

    print("Choose encoding options (e.g., '1,1,2' to apply URL encoding twice then HTML entity encoding):")
    print("1) URL encoding")
    print("2) HTML entity encoding")
    print("3) Hexadecimal encoding")
    print("4) Base64 encoding")
    choices = input("Enter your choices separated by commas (e.g., 1,2,3): ")

    # Mapping choices to encoding functions and names
    encoding_funcs = {
        '1': (encode_to_url, "URL"),
        '2': (encode_to_html_entity, "HTML"),
        '3': (encode_to_hex, "Hex"),
        '4': (encode_to_base64, "Base64")
    }

    # Split and validate the choices
    choice_list = [choice.strip() for choice in choices.split(',')]
    encoding_sequence_names = []  # To hold the names of the encoding types

    for choice in choice_list:
        if choice not in encoding_funcs:
            print(f"Invalid choice: {choice}")
            return
        encoding_sequence_names.append(encoding_funcs[choice][1])

    encoded_lines = []
    for line in lines:
        encoded_text = line.strip()
        for choice in choice_list:
            encode_func = encoding_funcs[choice][0]
            encoded_text = encode_func(encoded_text)  # Apply encoding step-by-step
        encoded_lines.append(encoded_text)

    # Create a descriptive file name
    encoding_sequence_str = "_".join(encoding_sequence_names)
    output_file_name = f"encoded_{encoding_sequence_str}_{file_name}"

    with open(output_file_name, 'w') as output_file:
        for encoded_line in encoded_lines:
            output_file.write(encoded_line + '\n')

    print(f"Encoded file saved as {output_file_name}")

if __name__ == "__main__":
    main()
