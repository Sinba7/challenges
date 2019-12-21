from data import DICTIONARY, LETTER_SCORES

def load_words(dictionary_path = DICTIONARY):
    """Load dictionary into a list and return list"""
    with open(dictionary_path, 'r') as f:
        return [word.strip() for word in f.readlines()] # strip remove the leading and tailing spaces from a string


def calc_word_value(word, letter_score_dict = LETTER_SCORES):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    # score = 0
    # for letter in word:
    #     if letter.upper() in LETTER_SCORES.keys():
    #         score += letter_score_dict[letter.upper()]
    # return score
    letter_to_score = [letter_score_dict[letter.upper()] for letter in word if letter.upper() in LETTER_SCORES.keys()]
    return sum(letter_to_score)
    

def max_word_value(word_list=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if not word_list:
        word_list = load_words()  
    ws_list = [{'word':word, 'score':calc_word_value(word)} for word in word_list]
    sorted_ws_list = sorted(ws_list, key=lambda ws:ws['score'], reverse=True)
    return sorted_ws_list[0]['word']

if __name__ == "__main__":
    pass # run unittests to validate
