import sys
import string

def calculate_char_sums(input_string):
    upper_sum = 0
    lower_sum = 0
    punct_sum = 0
    digit_sum = 0
    space_sum = 0

    for char in input_string:
        if char.isupper():
            upper_sum += 1
        elif char.islower():
            lower_sum += 1
        elif char in string.punctuation:
            punct_sum += 1
        elif char.isdigit():
            digit_sum += 1
        elif char.isspace():
            space_sum += 1

    print(f"Upper-case characters sum: {upper_sum}")
    print(f"Lower-case characters sum: {lower_sum}")
    print(f"Punctuation characters sum: {punct_sum}")
    print(f"Digits sum: {digit_sum}")
    print(f"Spaces sum: {space_sum}")

def main():
    if len(sys.argv) != 2:
        raise AssertionError("Please provide exactly one string argument.")
    else:
        input_string = sys.argv[1]
        calculate_char_sums(input_string)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        user_input = input("Please provide a string: ")
        calculate_char_sums(user_input)
    else:
        main()
