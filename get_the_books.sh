#!/bin/bash
# Array of book IDs
BOOK_IDS=(2147 2150 2148 2149 2145 2160 22500 28580 15143 32030)

# Base URL for downloading books from Project Gutenberg
BASE_URL="https://www.gutenberg.org/files"

# Create a directory to store the downloaded books
mkdir -p books

# Loop through each book ID and download the text
for ID in "${BOOK_IDS[@]}"
do
    wget -O "books/$ID.txt" "$BASE_URL/$ID/$ID-0.txt"
done


