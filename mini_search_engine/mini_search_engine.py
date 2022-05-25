import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s'
    ' - %(message)s')

logging.debug('Start of program' + f'\n')

# The user input is acted upon by the mini_search_engine function below.
# The make_inverse_index separates the document, by row, into words that
# may be searched by the user.
# The search function searches the index created by the make_inverse_index
# function for words queried by the user

def make_inverse_index(string_list):
    """This function creates our inverted index based on the document
a user wishes to search"""
    
    the_inverse_index = {}
    
    # The statement below takes in each line and its index, then it splits
    # the line into separate words 
    for line_number, line in enumerate(string_list):
        line_of_words = line.split()
        
        # The statements below takes in each each word from a given line and
        # assign to it an index corresponding to the row from which it was
        # retreived.
        for index, word in enumerate(line_of_words):
            the_inverse_index.setdefault(word, set()).add(line_number)
            
    return the_inverse_index
            
            
def search(inverted_index, word_query):
    """This function uses our inverted index to search for words in the
document the user wishes to search"""
    
    queries_answered = []
    
    # The following statements respond to user queries as to where they may
    # locate a word within a document of their choice
    for word in word_query:
        query_response = f'"{word}" in line(s) {inverted_index[word]}'
        queries_answered.append(query_response)
        
    return queries_answered


def mini_search_engine():
    """This function is called by the user, and the process of searching
through a desired document begins"""
    
    # The statements below separate the document into lines
    with open(input('Which text document would you like to search? Some'
        ' .txt documents have been provided for you, if you wish to observe'
        ' a demonstration of this program. Just type in the path to your'
        ' desired file: ')) as file:
        strings = list(file)
        make_inverse_index(strings)
        
        words_to_query = []
        
        while True:
            queried_word = input(
                'Type a word you are trying to find. '
                'If you have no further words for which to search '
                'press return. '
                )
            
            if not queried_word:
                break
            else:
                words_to_query.append(queried_word)
                
        print(search(make_inverse_index(strings), words_to_query))

mini_search_engine()