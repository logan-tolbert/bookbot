def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
        print(contents)


if __name__ == "__main__":  
    main()