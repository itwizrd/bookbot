#!/usr/bin/env python3
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
#    print(text)
    num_words = get_num_words(text)
#    print(num_words)
    num_char = get_num_char(text)
    #print(num_char)
    book_report = report(book_path, num_words, num_char)


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
def report(book_path, num_words, num_char):
    print(f'--- Begin report of {book_path} ---')
    print(f'{num_words} words found in the document')
    sorted_char=sorted(num_char.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_char:
        if char.isalpha():
            print(f'The "{char}" character was found {count} times')
    print('--- End Report ---')


main()