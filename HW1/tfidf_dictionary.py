import tfidf, os

class Dictionary():

    dictionary, sets = {}, {}
    features_save_path, dictionary_save_path = "", ""
    total_number_of_documents = 0

    def __init__(self, features_save_path, dictionary_save_path = ""):
        self.features_save_path = features_save_path
        self.dictionary_save_path = dictionary_save_path

    def add_word(self, _set, document, label, word):
        
        if _set not in self.sets:
            self.sets[_set] = {}

        if document not in self.sets[_set]:
            self.sets[_set][document] = {}
            self.sets[_set][document]['label'] = label
            self.sets[_set][document]['words'] = set()
            self.sets[_set][document]['number_of_words'] = 0
            self.total_number_of_documents += 1
        self.sets[_set][document]['number_of_words'] += 1
        self.sets[_set][document]['words'].add(word)

        if word not in self.dictionary:
            self.dictionary[word] = {}
            self.dictionary[word]['id'] = len(self.dictionary)-1
            self.dictionary[word]['docs'] = {}

        if document not in self.dictionary[word]['docs']:
            self.dictionary[word]['docs'][document] = 1
        else:
            self.dictionary[word]['docs'][document] += 1

    def get_feature_string_by_doc(self, _set, document):
        label = self.sets[_set][document]['label']
        line = "{} ".format(label)
        for word in self.sets[_set][document]['words']:
            line += "{}:{} ".format(self.dictionary[word]['id'],tfidf.tfidf(word, document, self))
        line += "\n"
        return line

    def get_word_frequency(self, word, document):
        return self.dictionary[word]['docs'][document]

    def get_number_of_words_in_document(self, document):
        for _set in self.sets:
            if document in _set:
                return self.sets[_set][document]['number_of_words']

    def get_number_of_document_word_occurs_in(self, word):
        return len(self.dictionary[word]['docs'])

    def get_total_number_of_documents(self):
        return self.total_number_of_documents

    def save_features_to_file(self):
        if not os.path.exists(self.features_save_path):
            os.makedirs(self.features_save_path)
        for s in self.sets:
            self.save_features_to_file_by_set(s)

    def save_features_to_file_by_set(self, _set):
        f = open(self.features_save_path + "features_" + _set, 'w')

        for document in self.sets[_set]:
            f.write(self.get_feature_string_by_doc(_set, document))

    def save(self):
        if not os.path.exists(self.dictionary_save_path) and self.dictionary_save_path != "":
            os.makedirs(self.dictionary_save_path)
        f = open(self.dictionary_save_path + "dictionary", 'w');
        f.write("{}\n".format(len(self.dictionary)))

        for word in self.dictionary:
            f.write("{}\t{}\n".format(self.dictionary[word]['id'], word))
