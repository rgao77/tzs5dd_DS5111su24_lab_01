#!/bin/bash
echo "Count of 'raven':"
grep -o 'raven' books/15951.txt | wc -l

echo "Count of 'Raven':"
grep -o 'Raven' books/15951.txt | wc -l

echo "Count of 'raven' (case insensitive):"
grep -i -o 'raven' books/15951.txt | wc -l

