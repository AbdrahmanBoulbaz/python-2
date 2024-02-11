import sys
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

def encode_to_morse(input_string):
    encoded_string = ""
    for char in input_string.upper():
        if char in morse_code_dict:
            encoded_string += morse_code_dict[char] + " "
    return encoded_string.strip()

def main():
    if len(sys.argv) != 2:
        print("Usage: python program_name.py \"string_to_encode\"")
    else:
        input_string = sys.argv[1]
        encoded_string = encode_to_morse(input_string)
        print(encoded_string)

if __name__ == "__main__":
    main()