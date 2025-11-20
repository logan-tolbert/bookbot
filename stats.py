def get_book_text(path):
    with open(path) as f:
        return f.read();

def get_word_count(text):
    words = text.split()
    return len(words);

def get_char_count(text):
    char_dict = {}
    chars = list(sorted(text.lower()))
    for char in chars:
        if char_dict.get(char) is None:
            char_dict[char] = chars.count(char)
        else: 
            continue
    return char_dict

def split_char_counts(char_dict):
    char_list = list()
    for item in char_dict.items():
        if item[0].isalpha():
            char_dict = {"char":item[0],"count":item[1]}
            char_list.append(char_dict)
        else: 
            continue
    return sorted(char_list,reverse=True, key=lambda c: c["count"])
    
def print_report(path):
    text = get_book_text(path)
    print(f"Analyzing book found at {path}...")
    print(f"----------- Word Count ----------")
    word_count = get_word_count(text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_count = split_char_counts(get_char_count(text))
    for item in char_count:
        print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")