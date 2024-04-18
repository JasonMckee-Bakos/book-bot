def main():
    bookPath = "books/frankenstein.txt"
    text = getText(bookPath)
    num_words = countWords(text)
    print(num_words)

def countWords(text):
    wordCount = text.split()
    return len(wordCount)

def getText(path):
       with open(path) as f:
        file_contents = f.read()
        return file_contents
    

main()
