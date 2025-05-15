def count_words(text):
    return len(text.split())

def count_characters(text):
    frequency = {}
    for char in text:
        char = char.lower()
        if char not in frequency:
            frequency[char] = 1
        else:
            frequency[char] += 1
    return frequency

def dictsort(dictionary):
    dictlist = []
    for word in dictionary:
        dictlist.append({"char": word, "num": dictionary[word]})
    dictlist.sort(reverse=True, key=lambda x: x["num"])
    return dictlist

