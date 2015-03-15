from __future__ import division

from sys import argv, exit
import os, math, fileutils

def get_word_index(word, dictionary):
    word = word.strip()
    if word not in dictionary:
        dictionary[word] = len(dictionary)

    return dictionary[word]

def save_set_feature_vector_to_file(set_name, documents, feature_save_path):
    f = open(feature_save_path + "feature_" + set_name, 'w')
    for document in documents:
        for c in document.keys():
            if c == 0:
                f.write("1 ")
            else:
                f.write("-1 ")
            for feature in document[c]:
                f.write("{}:{} ".format(feature[0], feature[1]))
        f.write("\n")

def get_words_by_document_path(path, punctuations, stopwords, dictionary):
    words = []

    firstLine = True
    with open(path, 'r') as f:
        for line in f:

            if not firstLine:
                line = tokenize_string( line.lower(), punctuations )
                for word in line.strip().split():
                    if word_should_be_indexed(word, stopwords):
                        words.append(get_word_index(word, dictionary))
            else:
                firstLine = False

    return words

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def word_should_be_indexed(word, stopwords):
    return word != '' and word not in stopwords and not is_number(word) and len(word) > 2 and len(word) < 20

def tokenize_string(string, punctuations):
    for punctuation in punctuations:
        string = string.replace(punctuation, " ")

    string = string.replace('\'', ' \'')
    return string

def increase_count(word, d):
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
    return d

def tfidf(term_count, doc_count, num_doc):
    return math.log(term_count + 1) * math.log(doc_count / num_doc + 1)

def save_dictionary(dictionary):
    f = open(os.getcwd() + "/dictionary", 'w')
    f.write(str(len(dictionary)) + "\n")

    for word in dictionary.keys():
        f.write("{} {}\n".format(word, dictionary[word]))

def extract_features(dictionary, punctuations, stopwords, feature_save_path, data_path):
    tfs = {}
    idf = {}

    for s in fileutils.get_documents_by_path(data_path):
        for i, c in enumerate(fileutils.get_documents_by_path(data_path + s + "/")):
            for document in fileutils.get_documents_by_path(data_path + s + "/" + c + "/"):
                tf = {}
                for word in get_words_by_document_path(data_path + s + "/" + c + "/" + document, punctuations, stopwords, dictionary):
                    tf = increase_count(word, tf)
                for word in tf:
                    idf = increase_count(word, idf)
                tfs[document] = tf

    for s in fileutils.get_documents_by_path(data_path):
        documents = []
        features = {}
        for i, c in enumerate(fileutils.get_documents_by_path(data_path + s + "/")):
            for document in fileutils.get_documents_by_path(data_path + s + "/" + c + "/"):
                entry = {}
                entry[i] = []
                for feature in tfs[document]:
                    entry[i].append( (feature, tfidf(tfs[document][feature], idf[feature], len(tfs))) )
                documents.append(entry)
        save_set_feature_vector_to_file(s, documents, feature_save_path)

def usage():
    print argv[0], "<data set> <stopwords file>"
    exit(1)

def generate_feature_files(data_path, stopwords_path):
    dictionary = {}
    punctuations = ["subject:", "re:", "=", "_", ":", ";", ".", "!", "?", ",", "(", ")", "<", ">", "-", "*", "\""]
    stopwords = fileutils.get_stopwords(stopwords_path)

    feature_save_path = "features/"
    if not os.path.exists(feature_save_path):
        os.makedirs(feature_save_path)
    
    extract_features(dictionary, punctuations, stopwords, feature_save_path, data_path)
    save_dictionary(dictionary)

if __name__ == '__main__':
    if len(argv) < 3:
        usage()

    generate_feature_files(argv[1], argv[2])

