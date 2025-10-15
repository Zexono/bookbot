from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
         file_contents = f.read()
    return file_contents




def main():
    file_path = "books/frankenstein.txt"
    txt = get_book_text(file_path)
    num = count_word(txt)
    chardict = count_char(txt)
    #print(f"Found {num} total words")
    charlist = dict_to_list(chardict)
    #print(charlist)
    charlist.sort(key=sort_char,reverse=True)
    #print(charlist)

    ##report print
    print("============ BOOKBOT ============")
    print("Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for char in charlist:
        if char["char"].isalpha() == False:
            continue
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")
main()
