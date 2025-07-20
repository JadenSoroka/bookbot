def get_book_text(fpath):
    with open(fpath) as f:
        return f.read()

def get_word_count(fpath):
    book_text = get_book_text(fpath)
    words = book_text.split()
    num_words = len(words)
    return num_words

def get_character_count(fpath):
    book_text = get_book_text(fpath)
    book_letters = list(line.strip().lower() for line in book_text)
    each_char = set(line.strip().lower() for line in book_text)
    char_count = {}
    char_count_list = []
    for char in each_char:
        letter_count = 0
        for letter in book_letters:
            if char == letter:
                letter_count += 1
        char_count[char] = letter_count

    for char in char_count:
        if char.isalpha():
            char_count_list.append({"char": char, "num": char_count[char]})

    def sort_on(item):
        return (item["num"])
    
    char_count_list.sort(reverse=True, key=sort_on)
    
    for line in char_count_list:
        print(f"{line["char"]}: {line["num"]}")
