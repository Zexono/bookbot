from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
         file_contents = f.read()
    return file_contents




def main():
    txt = get_book_text("books/frankenstein.txt")
    num = count_word(txt)
    chardict = count_char(txt)
    print(f"Found {num} total words")
    charlist = dict_to_list(chardict)
    #print(charlist)
    charlist.sort(key=sort_char,reverse=True)
    print(charlist)

main()
