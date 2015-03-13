from __future__ import division

import os
import math

punctuations = ["subject:", "re:", "=", "_", ":", ";", ".", "!", "?", ",", "(", ")", "<", ">", "-", "*", "\""]
stop_words = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

def get_word_index(word):

    word = word.strip()
    if word not in dictionary:
        dictionary[word] = len(dictionary)

    return dictionary[word]

def feature_file_path():
    return os.getcwd() + "/features/"

def save_set_feature_vector_to_file(set_name, documents):
    print "Saving {} to file ..".format(set_name)

    f = open(feature_file_path() + "feature_" + set_name, 'w')
    for document in documents:
        for c in document.keys():
            if c == 0:
                f.write("1 ")
            else:
                f.write("-1 ")
            for feature in document[c]:
                f.write("{}:{} ".format(feature[0], feature[1]))
        f.write("\n")

def get_documents_by_path(path):
    documents = os.listdir(path)
    documents.remove('.DS_Store')
    return documents

def add_word_to_dictionary(word, document_id):

    if word not in dictionary:
        entry = {'id' : len(dictionary), 'doc_count' : 0, 'frequency' : {}}
        dictionary[word] = entry;

    if document_id not in dictionary[word][frequency]:
        dictionary[word][frequency] = 1
    else:
        dictionary[word][frequency] += 1

def get_words_by_document_path(path):
    
    words = []

    f = open(path, 'r')

    for line in f:
        
        line = line.lower()
        line = tokenize_string(line)

        for word in line.strip().split():
            if word_should_be_indexed(word):
            
                index = get_word_index(word)
                words.append(index)

    return words

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def word_should_be_indexed(word):
    return word != '' and word not in stop_words and not is_number(word)

def tokenize_string(string):
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

data_path = os.getcwd() + '/data 1/'

dictionary = {}
tfs = {}
idf = {}

for s in get_documents_by_path(data_path):
    for i, c in enumerate(get_documents_by_path(data_path + s + "/")):
        for document in get_documents_by_path(data_path + s + "/" + c + "/"):
            tf = {}
            for word in get_words_by_document_path(data_path + s + "/" + c + "/" + document):
                tf = increase_count(word, tf)
            for word in tf:
                idf = increase_count(word, idf)
            tfs[document] = tf

for s in get_documents_by_path(data_path):
    documents = []
    features = {}
    for i, c in enumerate(get_documents_by_path(data_path + s + "/")):
        for document in get_documents_by_path(data_path + s + "/" + c + "/"):
            entry = {}
            entry[i] = []
            for feature in tfs[document]:
                entry[i].append( (feature, tfidf(tfs[document][feature], idf[feature], len(tfs))) )
            documents.append(entry)
    save_set_feature_vector_to_file(s, documents)

save_dictionary(dictionary)

