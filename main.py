import sys

from stats import count_words

from stats import count_characters

print(sys.argv)

def get_book_text(path_to_file):

    with open(path_to_file) as f:
    # do something with f (the file) here
    # f is a file object
        return f.read()

def main():

    path_to_file = sys.argv[1]

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text= get_book_text(sys.argv[1]) 
    

main()







    


    