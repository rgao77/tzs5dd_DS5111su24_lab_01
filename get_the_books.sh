#!/bin/bash
# Array of book IDs
BOOK_IDS=(2147 2150 2148 2149 2145 2146 25200 15951 14082 36572)

# Base URL for downloading books from Project Gutenberg
BASE_URL="https://www.gutenberg.org/files"

# Create a directory to store the downloaded books
mkdir -p books

# Loop through each book ID and download the text
for ID in "${BOOK_IDS[@]}"
do
    wget -O "books/$ID.txt" "$BASE_URL/$ID/$ID-0.txt"
done

