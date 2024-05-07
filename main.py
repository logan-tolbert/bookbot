from sys import argv

script, f_path = argv

def main():
    text = get_content(f_path)
    word_count = count_words(text)
    # Prints content of file to terminal
    # print(text)
    print(f"Word count: {word_count}")


def get_content(path):
     with open(path) as f:
        text = f.read()
        return(text)


def count_words(text):
    words = text.split()
    return(len(words))

main()

