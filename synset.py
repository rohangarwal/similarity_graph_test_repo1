class Synset:
    '''
    '''

    #not sure when to initiliaze below params
    def __init__(self,definition,edges,lemmas,examples):
        '''
            definition - str
            lemma_names - list of unicode values
            examples - list of unicode values
            edges =-
        '''
        self.definition = definition
        self.edges = edges
        self.lemma_names = lemma_names
        self.examples = examples



class Noun(Synset):
    '''
    '''

    def __init__(self,definition,edges,lemmas,examples):
        Synset.__init__(self,definition,edges,lemmas,examples)
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

class Verb(Synset):
    def __init__(self,definition,edges,lemmas,examples):
        Synset.__init__(self,definition,edges,lemmas,examples)

class Adjective(Synset):
    def __init__(self,definition,edges,lemmas,examples):
        Synset.__init__(self,definition,edges,lemmas,examples)

class Adverb(Synset):
    def __init__(self,definition,edges,lemmas,examples):
        Synset.__init__(self,definition,edges,lemmas,examples)
