def main():
    bookPath = "books/frankenstein.txt"
    text = getText(bookPath)
    num_words = countWords(text)
    charCount = count_characters(text)

    print(charCount)

def countWords(text):
    wordCount = text.split()
    return len(wordCount)

def getText(path):
       with open(path) as f:
        file_contents = f.read()
        return file_contents
       
def count_characters(text):
    charDict = {}
    for char in text.lower():
        if char not in charDict:
            charDict[char] = 1
        else:
            charDict[char] += 1
    return charDict

main()
