from __future__ import division
from random import shuffle

import numpy as np

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


