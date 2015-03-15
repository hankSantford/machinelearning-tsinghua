from __future__ import division

import os
import numpy as np

from random import shuffle

dictionary_path = '/dictionary'

feature_path = '/features/'
set_names = ['feature_s1', 'feature_s2', 'feature_s3', 'feature_s4', 'feature_s5']

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
                f = np.zeros((dictionary_size, 1))
                for i in xrange(1,len(data)):
                    (index, value) = data[i].split(":")
                    index = int(index)
                    value = float(value)
                    f[index,0] = value
                data_set.append((c, f))
     return data_set

class Perception():
    def __init__(self, learning_rate, num_features):
        self.learning_rate = learning_rate
        self.tp = 0
        self.fp = 0
        self.tn = 0
        self.fn = 0
        self.w = np.zeros((num_features, 1))

    def train(self, training_set):
        for i in xrange(0,100):
            shuffle(training_set)
            for sample in training_set:
                self.train_sample(sample[0], sample[1])

    def train_sample(self, classification, features):
        if classification * np.dot(np.transpose(self.w), features) <= 0:
            self.w += self.learning_rate * classification * features

    def test(self, test_set):
        shuffle(test_set)
        for sample in test_set:
            self.test_sample(sample[0], sample[1])

    def test_sample(self, classification, features):
        v = np.dot( np.transpose( self.w ), features )
        if v <= 0:
            if classification == -1:
                self.tn += 1
            else:
                self.fn += 1
        else:
            if classification == 1:
                self.tp += 1
            else:
                self.fp += 1

    def get_results(self):
        return (self.precision(), self.recall(), self.f1())

    def precision(self):
        return self.tp / (self.tp + self.fp)

    def recall(self):
        return self.tp / (self.tp + self.fn)

    def f1(self):
        precision = self.precision()
        recall = self.recall()
        return 2 * precision * recall / (precision + recall)

def print_results(precision, recall, f1):
    print "Precision:", precision
    print "Recall:", recall
    print "F1 score:", f1

dictionary_size = get_dictionary_size(dictionary_path)
avg_precision = 0
avg_recall = 0
avg_f1 = 0

for i in xrange(0,len(set_names)):
    p = Perception(0.1, dictionary_size)
    training_set_names = set_names[:]
    test_set_names = [training_set_names.pop(i)]
    training_set = get_data_set(training_set_names, dictionary_size)
    test_set = get_data_set(test_set_names, dictionary_size)

    print "Training sets:", training_set_names
    print "Test set:", test_set_names
    p.train(training_set)
    p.test(test_set)
    (precision, recall, f1) = p.get_results()

    print_results(precision, recall, f1)
    avg_precision += precision / len(set_names)
    avg_recall += recall / len(set_names)
    avg_f1 += f1 / len(set_names)

    print ""

print_results(avg_precision, avg_recall, avg_f1)
