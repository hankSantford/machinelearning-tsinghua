# Input: feature files s1 to s5
# Steps:
# Set i=1, take s_i as test set and others as training set.

# On the training set, learn the parameters theta of the logistic regression function and save the learnt parameters (see more details in the following 2 pages).

# On the test set, using the parameters theta learnt from Step 2 to classify each document as hockey or baseball (see more details in the following 2 pages).

# Calculate Precision, Recall and F1 score.

# i++ , Repeat Step 1, 2, 3, and 4 util i > 5.

import os
import numpy as np

feature_files_path = os.getcwd() + "/features/"
feature_files = ["feature_s1", "feature_s2", "feature_s3", "feature_s4", "feature_s5"]
#training_set = ["feature_example_s1"]

test_set = feature_files[0]
training_set = feature_files[1:5]

# w_size = 32768
w_size = 30042

alpha = 0.5

def get_feature_vector(feature_vector):
    # print "getting feature vector"
    v = np.zeros((w_size,1))
    for f in feature_vector:
        (feature, value) = f.split(":")
        # print int(feature), value
        v[int(feature),0] = value
    # print sum(v)
    return v

def h(x, theta):
    # print sum(theta), sum(x), np.dot(np.transpose(theta),x)
    dot = np.dot(np.transpose(theta),x)[0,0]
    # print dot
    h = 1.0 / (1.0 + np.exp(- dot ))
    # print h
    return h

w = np.zeros((w_size,1))

for s in training_set[:1]:
    i = 0
    f = open(feature_files_path + s, "r")
    for line in f:
        features = line.strip().split(" ")
        if features[0] == "baseball":
            label = 1.0
        else:
            label = -1.0
        feature_vector = get_feature_vector(features[1:])
        # print feature_vector
        i+=1
        for d in xrange(0,w_size):
            # print ( label - h(feature_vector, w) ) * feature_vector[d,0]
            # print d
            if feature_vector[d,0] != 0:
                
                w[d] += alpha * label * feature_vector[d, 0]
        
        print i

f = open(feature_files_path + test_set, "r")
for line in f:
    features = line.strip().split(" ")
    feature_vector = get_feature_vector(features[1:])
    print np.dot(np.transpose(w), feature_vector)[0,0] > 0
