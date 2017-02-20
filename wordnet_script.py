from nltk.corpus import wordnet as wn

class Wordnet:
    def __init__(self,callback):
        self.callback = callback
        #self.callback2 = callback2
        self.all_lemmas = None

    def initiliaze_lemma_list(self):
        self.all_lemmas = wn.all_lemma_names()

    def get_word(self):
        lemma = self.all_lemmas.next()
        self.callback(lemma)
