import shelve
if __name__ == "__main__":
    d = shelve.open('label_to_word_object')
    for key in d.keys():
        print key
        print '--------------'
        print d[key].nouns
        print '***************'
