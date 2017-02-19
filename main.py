from wordnet_script import Wordnet

def make_words(word):
    

if __name__ == "__main__":
    wordnet = Wordnet(make_words)
    while True:
        try:
            wordnet.get_words()
        except Exception as e:
            #handle_error()
            raise StopIteration()
