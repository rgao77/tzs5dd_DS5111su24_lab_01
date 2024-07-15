#!/bin/bash
# Array of book IDs and their correct file names
BOOK_IDS=(
    "17192" "17192.txt"
    "932" "932.txt"
    "1063" "1063.txt"
    "10031" "10031-0.txt"
    "14082" "14082-0.txt"
)

# Base URL for downloading books from Project Gutenberg
BASE_URL="https://www.gutenberg.org/files"

# Create a directory to store the downloaded books
mkdir -p books

# Loop through each book ID and download the text
for ((i=0; i<${#BOOK_IDS[@]}; i+=2))
do
    ID=${BOOK_IDS[i]}
    FILE=${BOOK_IDS[i+1]}
    wget -O "books/$ID.txt" "$BASE_URL/$ID/$FILE" || echo "Failed to download $ID"
done

