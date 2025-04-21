import sys

if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        

def count_words(path_to_file):
   
    with open(path_to_file) as f:
        book_as_string= f.read()
    split=book_as_string.split()        
    word_count=len(split)
    print (f" Found {word_count} total words")

# Call the function
count_words(sys.argv[1])

def count_characters (path_to_file):
    with open(path_to_file) as f:
        book_as_string= f.read()
    all_lower=book_as_string.lower()
    
    num_characters={}
    for character in all_lower:
        if character in num_characters:
            num_characters[character]+=1
        else:
            num_characters[character]=1
    
    return num_characters

count_characters(sys.argv[1])
character_counts = count_characters(sys.argv[1])

def make_only_alpha(non_alpha_list):

# Create a new dictionary containing only alphabetic keys
    filtered_counts = {char: count for char, count in non_alpha_list.items() if char.isalpha()}

    return filtered_counts
# Output: {'a': 10, 'b': 5}


only_alpha_dict=make_only_alpha(character_counts)

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list_with_symbols= []
    for ch in num_chars_dict:
        sorted_list_with_symbols.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list_with_symbols.sort(reverse=True, key=sort_on)
    

    for item in sorted_list_with_symbols:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    

    
# [{'name': 'plane', 'num': 10}, {'name': 'car', 'num': 7}, {'name': 'boat', 'num': 2}]
chars_dict_to_sorted_list(only_alpha_dict)

