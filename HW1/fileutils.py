from os import listdir
import numpy as np

def get_documents_by_path(path):
    """Returns a list with document at the specified path.

    path - path of the folder which should be listed
    """
    documents = listdir(path)
    if '.DS_Store' in documents:
        documents.remove('.DS_Store')
    return documents

def get_stopwords(stopwords_path):
    """Returns a list of stopwords.

    stopwords_path - path to the stopwords file
    """
    stopwords = []
    with open(stopwords_path) as f:
        for line in f:
            stopwords.append(line.strip());

    return stopwords

def get_data_set(feature_path, data_set_names, dictionary_size):
    """Returns a list of samples, given the path and the data set names.

    feature_path - path to the features
    data_set_names - list of names for the data data sets
    dictionary_size - size of the dictionary
    """

    data_set = []

    for data_set_name in data_set_names:
        with open(feature_path + data_set_name, 'r') as f:
            for line in f:
                data = line.strip().split()
                c = int(data[0])
                f = np.zeros((dictionary_size, 1))
                for i in xrange(1,len(data)):
                    (index, value) = data[i].split(":")
                    index = int(index)
                    value = float(value)
                    f[index,0] = value
                data_set.append((c, f))
    return data_set

def get_dictionary_size(path):
    """Returns the size of the dictionary.

    path -  path to the dictionary file
    """
    with open(path, 'r') as f:
        size = int(f.readline().strip())
        return size