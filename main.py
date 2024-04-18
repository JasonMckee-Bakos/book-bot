def main():
    bookPath = "books/frankenstein.txt"
    text = getText(bookPath)
    num_words = countWords(text)
    charCount = count_characters(text)
    chars_list_sorted = sortedList(charCount)
    print(f"--- Begin report of {bookPath} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_list_sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


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

def sortedList(chars):
    newList = []
    for char in chars:
        newList.append({"char": char, "num": chars[char]})
    newList.sort(reverse=True, key=sort_on)
    return newList

def sort_on(dict):
        return dict["num"]

main()
