

def get_num_words(book):
    with open(book) as f:
        file_contents = f.read()
        num_words = len(file_contents.split())
        return num_words


def char_appearance(book):
    char = {}
    with open(book) as f:
        file_contents = f.read().lower()
        file_char = list(file_contents)
        for c in file_char:
            if c in char:
                char[c] += 1
            else:
                char[c] = 1
    return char
