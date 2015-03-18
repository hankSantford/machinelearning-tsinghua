from sys import argv, exit
from tfidf_dictionary import Dictionary
import fileutils

def get_words_by_document_path(path, punctuations, stopwords):
    """Returns a list of words given by the path to the document

    path - path to the document
    punctuations - list of punctuations
    stopwords - list of stopwords
    """

    words = []

    firstLine = True
    with open(path, 'r') as f:
        for line in f:

            if not firstLine:
                line = tokenize_string( line.lower(), punctuations )
                for word in line.strip().split():
                    if word_should_be_indexed(word, stopwords):
                        words.append(word)
            else:
                firstLine = False

    return words

def is_number(s):
    """Returns if the specified string is a number."""
    try:
        float(s)
        return True
    except ValueError:
        return False

def word_should_be_indexed(word, stopwords):
    """Returns True if the word should be indexed."""
    return word != '' and word not in stopwords and not is_number(word) and len(word) > 2 and len(word) < 20

def tokenize_string(string, punctuations):
    """Returns a tokenized string."""
    for punctuation in punctuations:
        string = string.replace(punctuation, " ")

    string = string.replace('\'', ' \'')
    return string

def generate_features(data_path, features_save_path, dictionary_save_path, stopwords):

    punctuations = ["subject:", "re:", "=", "_", ":", ";", ".", "!", "?", ",", "(", ")", "<", ">", "-", "*", "\""]
    dictionary = Dictionary(features_save_path, dictionary_save_path)

    for s in fileutils.get_documents_by_path(data_path):
        for c in fileutils.get_documents_by_path(data_path + s + "/"):
            for document in fileutils.get_documents_by_path(data_path + s + "/" + c + "/"):
                for word in get_words_by_document_path(data_path + s + "/" + c + "/" + document, punctuations, stopwords):
                    if c == 'baseball':
                        label = 1
                    else:
                        label = -1
                    dictionary.add_word(s, document, label, word)

    dictionary.save_features_to_file()
    dictionary.save()
    


