#!/usr/bin/env python3
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
#    print(text)
    num_words = get_num_words(text)
    print(num_words)

def get_book_text(path):
    with open(path) as file:
        return file.read()
def get_num_words(input_file):
    words = input_file.split()
    return len(words)
    

main()