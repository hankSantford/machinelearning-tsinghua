from __future__ import division
import math

def tfidf(word, document, dictionary):
    """Returns the tf-idf score."""
    return tf(word, document, dictionary) * idf(word, dictionary)

def tf(word, document, dictionary):
    """Returns the term frequency score."""
    word_frequency = dictionary.get_word_frequency(word, document)
    number_of_words_in_document = dictionary.get_number_of_words_in_document(document)
    return math.log(1 + word_frequency)

def idf(word, dictionary):
    """Returns the inverse document freqquency score."""
    number_of_document_word_occurs_in = dictionary.get_number_of_document_word_occurs_in(word)
    total_number_of_documents = dictionary.get_total_number_of_documents()
    return math.log(total_number_of_documents / number_of_document_word_occurs_in + 1)