from stats import get_num_words
from stats import get_num_chars
from stats import dict_to_list

"""
This function takes a filepath and returns its text content.
"""
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    #filepath = './books/frankenstein.txt'
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = get_num_words(book_text)
    word_dict = get_num_chars(book_text)
    data_list = dict_to_list(word_dict)
    output_str = "============ BOOKBOT ============\n"
    output_str += "Analyzing book found at books/frankenstein.txt...\n"
    output_str += "----------- Word Count ----------\n"
    output_str += num_words + "...\n"
    output_str += "--------- Character Count -------\n"
    for d in data_list:
        if d['char'].isalpha():
            output_str = output_str + f"{d['char']}: {d['num']}\n"
    output_str = output_str + "============= END ==============="
    print(output_str)

main()