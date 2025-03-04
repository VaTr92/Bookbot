def word_count_from_text(text):
    words = text.split()
    word_count = len(words)
    return word_count

def character_count_from_text(text):
    dict_chars = {}
    text_lower = text.lower()
    for char in text_lower:
        if char.isalpha():
            dict_chars[char] = dict_chars.get(char, 0) + 1
    return dict_chars


def sorter(char_dict):
    sorted_char_list = list(char_dict.items())
    sorted_char_list.sort(key=lambda x: x[1], reverse=True)
    return sorted_char_list