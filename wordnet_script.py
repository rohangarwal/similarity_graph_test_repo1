from nltk.corpus import wordnet as wn

class Wordnet:
    def __init__(self,callback):
        self.callback = callback

    def get_words(self):
        words = wn.all_lemma_names()
        self.callback(words.next)
