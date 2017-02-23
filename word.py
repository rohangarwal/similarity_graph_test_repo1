class Word:
    '''
    '''

    def __init__(self,label):
        self.label = label
        self.domain
        self.nouns = list()
        self.verbs = list()
        self.adjectives = list()
        self.adverbs = list()

    def populate_lists():
        pass

    def __str__(self):
        return self.label + ';' + str(self.nouns) + ';' + str(self.verbs) + ';' \
            + str(self.adjectives) + ';' + str(self.adverbs)
