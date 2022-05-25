#---Task 0_6_6, 0_6_7, and 0_6_8 p.36 (To the best of my interpretation)
def make_inverse_index(string_list):
    """This function creates our inverted index based on the document
a user wishes to search"""
    the_inverse_index = {}
    for line_number, line in enumerate(string_list):
        line_of_words = line.split()
        for index, word in enumerate(line_of_words):
            the_inverse_index.setdefault(word, set()).add(line_number)
    return the_inverse_index
            
def search(inverted_index, word_query):
    """This function uses our inverted index to search for words in the
document user wishes to search"""
    queries_answered = []
    for word in word_query:
        query_response = f'"{word}" in line(s) {inverted_index[word]}'
        queries_answered.append(query_response)
    return queries_answered

def mini_search_engine():
    """This function is called by the user, and the process of searching
through a desired document begins"""
    with open(input('Which text document would you like to search? ')) as file:
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