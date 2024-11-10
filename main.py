def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
        print(count_words(contents))
        

def count_words(text):
    return len(text.split())

if __name__ == "__main__":  
    main()