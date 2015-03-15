from sys import argv, exit
from perception import Perception

import tfidf, fileutils

dictionary_path = 'dictionary'
feature_path = 'features/'

def print_results(precision, recall, f1):
    print "Precision:", precision
    print "Recall:", recall
    print "F1 score:", f1

def usage():
    print argv[0], "<data set> <stopwords file> [-D]"
    exit(1)

if __name__ == '__main__':
    if len(argv) < 3:
        usage()

    if "-D" not in argv:
        print "Generating feature files .."
        tfidf.generate_feature_files(argv[1], argv[2])

    print "Starting training .."

    set_names = fileutils.get_documents_by_path(feature_path)
    dictionary_size = fileutils.get_dictionary_size(dictionary_path)
    avg_precision = 0
    avg_recall = 0
    avg_f1 = 0

    p = Perception(0.25, dictionary_size)

    for i in xrange(0,len(set_names)):

        print "=" * 10, "EPOCH", i+1 , "=" * 10

        training_set_names = set_names[:]
        test_set_names = [training_set_names.pop(i)]
        training_set = fileutils.get_data_set(feature_path, training_set_names, dictionary_size)
        test_set = fileutils.get_data_set(feature_path, test_set_names, dictionary_size)

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

    print "=" * 10, "Average results", "=" * 10 
    print_results(avg_precision, avg_recall, avg_f1)

