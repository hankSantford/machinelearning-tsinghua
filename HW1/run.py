from sys import argv, exit
from perception import Perception
import tfidf_generate_features, fileutils

features_save_path = "features/"
dictionary_save_path = ""

def print_results(precision, recall, f1):
    """Prints the results in a satisfying way."""
    print "Precision:", precision
    print "Recall:", recall
    print "F1 score:", f1

def usage():
    print argv[0], "<data set> <stopwords file> [-D]"
    exit(1)

# if number of arguments is too short, print usage
if __name__ == '__main__':
    if len(argv) < 3:
        usage()

    # if the program is run with the -D argument, the existing dictionary file is used
    if "-D" not in argv:
        print "Generating feature files .."
        stopwords = fileutils.get_stopwords(argv[2])
        tfidf_generate_features.generate_features(argv[1], features_save_path, dictionary_save_path, stopwords)

    print "Starting training .."

    # get the names for the sets
    set_names = fileutils.get_documents_by_path(features_save_path)
    dictionary_size = fileutils.get_dictionary_size(dictionary_save_path + "dictionary")
    avg_precision, avg_recall, avg_f1 = 0,0,0

    for i in xrange(0,len(set_names)):

        p = Perception(0.25, dictionary_size)

        print "=" * 10, "EPOCH", i+1 , "=" * 10

        # get the sets for training and testing
        training_set_names = set_names[:]
        test_set_names = [training_set_names.pop(i)]
        training_set = fileutils.get_data_set(features_save_path, training_set_names, dictionary_size)
        test_set = fileutils.get_data_set(features_save_path, test_set_names, dictionary_size)

        print "Training sets:", training_set_names
        print "Test set:", test_set_names

        # train and test
        p.train(training_set)
        p.test(test_set)
        (precision, recall, f1) = p.get_results()

        # prints the results and calc the avg results
        print_results(precision, recall, f1)
        avg_precision += precision / len(set_names)
        avg_recall += recall / len(set_names)
        avg_f1 += f1 / len(set_names)

        print ""

    print "=" * 10, "Average results", "=" * 10 
    print_results(avg_precision, avg_recall, avg_f1)

