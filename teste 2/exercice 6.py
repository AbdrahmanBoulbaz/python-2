import string

def print_words_longer_than_n(S, N):
    if not isinstance(S, str) or not isinstance(N, int):
        print("Error: Both arguments must be a string and an integer.")
        return

    S_cleaned = ''.join(char for char in S if char not in string.punctuation)

    
    words = S_cleaned.split()
    filtered_words = [word for word in words if len(word) > N]
    print(filtered_words)


if __name__ == "__main__":
    S = "Hello, world! This is a test string. It has some words longer than 3 characters."
    N = 3
    print_words_longer_than_n(S, N)
