import os
from text_processor import clean_text, tokenize

def calculate_token_count(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    cleaned_text = clean_text(text)
    tokens = tokenize(cleaned_text)
    return len(tokens)

def main():
    files = [
        "books/17192.txt",
        "books/932.txt",
        "books/1063.txt",
        "books/10031.txt",
        "books/14082.txt"
    ]

    for file_path in files:
        if os.path.exists(file_path):
            count = calculate_token_count(file_path)
            print(f"{file_path}: {count} tokens")
        else:
            print(f"{file_path} not found.")

if __name__ == "__main__":
    main()

