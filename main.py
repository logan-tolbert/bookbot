#!/usr/bin/env python3
from sys import argv



script, f_path = argv

def main():
    text = get_content(f_path)
    word_count = count_words(text)
    charDict = count_chars(text)
    sortedCharlst = dict_to_sortd_lst(charDict)

    print(f"--- Begin report of {f_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in sortedCharlst:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_content(path):
     with open(path) as f:
        text = f.read()
        return(text)


def count_words(text):
    words = text.split()
    return(len(words))


def count_chars(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dictionary):
    return dictionary["num"]


def dict_to_sortd_lst(charDict):
    sorted_list = []
    for ch in charDict:
        sorted_list.append({"char": ch, "num": charDict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()

