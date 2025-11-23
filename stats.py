def word_count(words):
    num_words = words.split()
    return len(num_words)


def character_count(character):
    char_count = {}
    for x in character:
        x = x.lower()
        if x not in char_count:
            char_count[x] = 1
        else:
            char_count[x] += 1
    return char_count


def sorted_list(char_dict):
    char_list = []
    for x, y in char_dict.items():
        temp = dict(char=x, num=y)
        char_list.append(temp)
    char_list.sort(reverse=True, key=sort_on)
    return char_list


def sort_on(item):
    return item["num"]
