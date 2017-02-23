from wordnet_script import Wordnet
from nltk.corpus import wordnet as wn
from word import Word
from synset import Synset
from synset import Noun
from synset import Verb
from synset import Adjective
from synset import Adverb
import shelve
from synset import make_synsets

label_to_word_object = shelve.open('label_to_word_object')
wn_synset_to_synset_object = shelve.open('wn_synset_to_synset_object')

def make_words_and_synsets(word):
    new_word = Word(label=word)
    #print type(word)
    word = str(word)
    make_synsets(word)
    '''
    #print type(str(wn.synsets(word)[0].pos()))
    for synset in wn.synsets(word):
        #print synset
        if str(synset.pos()) == 'n':
            #noun synset
            new_word.nouns.append(Noun(
            definition=str(synset.definition()),edges=[],lemmas=synset.lemma_names(),examples=synset.examples()))

        elif str(synset.pos()) == 'v':
            #verb synset
            new_word.verbs.append(Verb(
            definition=str(synset.definition()),edges=[],lemmas=synset.lemma_names(),examples=synset.examples()))

        elif str(synset.pos() == 'a'):
            #adjective synset
            new_word.adjectives.append(Adjective(
            definition=str(synset.definition()),edges=[],lemmas=synset.lemma_names(),examples=synset.examples()))

        elif str(synset.pos() == 'r'):
            #Adverb synset
            new_word.adjectives.append(Adjective(
            definition=str(synset.definition()),edges=[],lemmas=synset.lemma_names(),examples=synset.examples()))

        else:
            print 'Error, POS not found!'
    '''
    label_to_word_object[word] = new_word

def handle_error():
    print 'all words done, closing dictionary'
    label_to_word_object.close()

def print_shelve_dictionary(filename):
    d = shelve.open(filename)
    for key in d.keys():
        print key + " : " + d[key]

if __name__ == "__main__":
    wordnet = Wordnet(make_words_and_synsets)
    wordnet.initiliaze_lemma_list()
    while True:
        try:
            wordnet.get_word()
        except StopIteration as e:
            handle_error()
