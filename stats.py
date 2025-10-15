def count_word(file):
    num_word = 0
    all_word = file.split()
    for word in all_word:
        num_word += 1
    return num_word

def count_char(file):
        
    a_z_dict = {}
    txt = file.lower()
    for char in txt:
        if char not in a_z_dict:
            a_z_dict[char] = 1
        else:
            a_z_dict[char] += 1
    
    return a_z_dict



def dict_to_list(dict):
    list_dict = []

    for char in dict:
        num = dict[char]
        list_dict.append({"char":char,"num":num})
    return list_dict


def sort_char(item):
    return item["num"]




