from nltk.corpus import wordnet as wn
import shelve

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
        self.lemma_names = lemmas
        self.examples = examples



class Noun(Synset): #NounSynset
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

def make_synsets(word):
    synset_object_hash = shelve.open('synset_object_hash')
    print '#############################################'
    for synset in wn.synsets(word):
        if(str(synset.pos()) == 'n'):
            synset_object_hash['a'] = Noun(definition=synset.definition(), edges=[], lemmas=synset.lemma_names(), examples=synset.examples())

    synset_object_hash.close()

def print_shelve_dictionary(filename):
    d = shelve.open(filename)
    for key in d.keys():
        print key + " : " + d[key].definition
if __name__ == "__main__":
    print_shelve_dictionary(filename='synset_object_hash')
