def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
        print(f"Word Count: {count_words(contents)}")
        print(f"Character Occurences: {count_char_occurence(contents)}")
        

def count_words(text):
    return len(text.split())

def count_char_occurence(text):
    char_count = {}
    for char in text.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

if __name__ == "__main__":  
    main()