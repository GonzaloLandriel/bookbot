def count_words(path_to_file):
    with open(path_to_file) as f:
        book_as_string= f.read()
    split=book_as_string.split()        
    word_count=len(split)
    print (f" Found {word_count} total words")

# Call the function
count_words("books/frankenstein.txt")

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

count_characters("books/frankenstein.txt")
character_counts = count_characters("books/frankenstein.txt")

def make_only_alpha(non_alpha_list):

# Create a new dictionary containing only alphabetic keys
    filtered_counts = {char: count for char, count in non_alpha_list.items() if char.isalpha()}

    print(filtered_counts)
    print(type(filtered_counts))
# Output: {'a': 10, 'b': 5}
make_only_alpha(character_counts)






