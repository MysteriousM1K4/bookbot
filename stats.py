def get_text_word_count(string):
    words = string.split(" ")
    return len(words)

def get_letter_count(string):
    count = {}
    for char in string:
        if not char.lower() in count:
            count[char.lower()] = 0
        count[char.lower()] += 1
    return count
