def count_words(bookstring):
    total_words = len(bookstring.split())
    return total_words

def count_letters(bookstring):
    letters_dic = {}
    for letter in bookstring:
        letter_low = letter.lower()
        if letter_low in letters_dic:
            letters_dic[letter_low] += 1
        else:
            letters_dic[letter_low] = 1
    return letters_dic

def sort_on(items):
    return items["num"]

def char_count_sorted(letter_count_dict):
    letter_count_list = []
    for key,num in letter_count_dict.items():
        if key.isalpha():
            letter_count_list.append({
                "char": key,
                "num": num
            })
    letter_count_list.sort(key=sort_on, reverse=True)
    return letter_count_list
            
def list_to_dict(dict_list):
    return {item["char"]: item["num"] for item in dict_list}
