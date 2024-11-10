def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
        generate_report(contents)
        
        
def count_words(text):
    return len(text.split())


def count_alphabetic_chars(text):
    char_count = {}
    for char in text.lower():
        if not char.isalpha():
            continue
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count


def generate_report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document")
    print()
    for char, count in count_char_occurrence(text).items():
        print(f"The '{char}' was found {count} times")
    print("--- End report ---")
    
    
if __name__ == "__main__":  
    main()