class Synset:
    '''
    '''

    #not sure when to initiliaze below params
    def __init__(self):
        self.meaning =
        self.edges =
        self.lemmas =
        self.examples =



class Noun(Synset):
    '''
    '''

    def __init__(self):
        Synset.__init__(self,meaning,edges,lemmas,examples)
        self.hypernyms = list()
        self.hyponyms = list()
        self.meronyms = list()

    def populate_lists(self,values,type):
        if type == 'hypernyms':
            self.hypernyms.extend(values)
        elif type == 'hyponyms':
            self.hyponyms.extend(values)
        elif type == 'meronyms':
            self.meronyms.extend(values)
