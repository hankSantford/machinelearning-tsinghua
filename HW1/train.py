import os
import numpy as np

from random import shuffle

dictionary_path = '/dictionary'

feature_path = '/features/'
training_set_names = ['feature_s1', 'feature_s2', 'feature_s3', 'feature_s4']
test_set_names = ['feature_s5']

# def load_dictionary(path):
#     dictionary = {}

#     with open(os.getcwd() + path, 'r') as f:
#         for line in f:
#             (word, index) = line.strip().split()
#             dictionary[word] = index

#     return dictionary

def get_dictionary_size(path):
    with open(os.getcwd() + path, 'r') as f:
        size = int(f.readline().strip())
        return size

def get_data_set(data_set_names, dictionary_size):

    data_set = []

    for data_set_name in data_set_names:

        with open(os.getcwd() + feature_path + data_set_name, 'r') as f:
            for line in f:
                data = line.strip().split()
                c = int(data[0])
                f = np.ones((dictionary_size, 1))
                for i in xrange(1,len(data)):
                    (index, value) = data[i].split(":")
                    index = int(index)
                    value = float(value)
                    f[index,0] = value
                data_set.append((c, f))
                # print c, sum(f)
    return data_set

dictionary_size = get_dictionary_size(dictionary_path)
training_set = get_data_set(training_set_names, dictionary_size)
test_set = get_data_set(test_set_names, dictionary_size)

shuffle(training_set)
shuffle(test_set)

print dictionary_size

print training_set[0]
