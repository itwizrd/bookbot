#!/usr/bin/env python3
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
#    print(text)
    num_words = get_num_words(text)
#    print(num_words)
    num_char = get_num_char(text)
    print(num_char)

def get_book_text(path):
    with open(path) as file:
        return file.read()
def get_num_words(input_file):
    words = input_file.split()
    return len(words)
def get_num_char(text):
    lower = text.lower()
    char_dict = {}
    for i in lower:
        char_dict[i] = char_dict.get(i,0) + 1
    return char_dict

#    make a dictionary from lower string. key = letter, value = count?
#    incriment each letter. for loop
#    return dictionary

main()