"""
This function takes a string and returns the number of words in it.
"""
def get_num_words(str):
    words = str.split()
    return f"Found {len(words)} total words"

"""
This function takes a string and returns a dictionary containing the 
number of each character in it.
"""
def get_num_chars(str):
    chars = {}
    for char in str.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

"""
This function takes a dictionary and returns a sorted list of dictionaries
"""
def dict_to_list(dict):
    list_of_dicts = []
    for key in dict.keys():
        num = dict[key]
        #print(f"appending key {key} and num {num}")
        list_of_dicts.append({ "char": key, "num": num })
        list_of_dicts.sort(reverse=True, key=sort_on)
        #print(list_of_dicts)
    return list_of_dicts