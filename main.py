def get_book_text(path_to_file):

    with open(path_to_file) as f:
    # do something with f (the file) here
    # f is a file object
        return f.read()

def main():
    text= get_book_text("books/frankenstein.txt") 
    

main()



from stats import count_words

from stats import count_characters



    


    