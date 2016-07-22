from __future__ import division
import time

MAX_LENGTH = 6

def combine(words):
    print words

def filter_words(words, length=MAX_LENGTH):
    '''
    Return a list that contains the words having the given length
    :param words:
    :param length:
    :return:
    '''
    return [word for word in words if len(word) == length] # use list comprehension

def is_composed_of_sub_words(word, words):
    '''
    Iterate over the given word by splitting it multiple times
    Then, look for small words into word list
    :param word:
    :param words:
    :return:
    '''
    sub = []
    for i in range(1, len(word)):
        part = dict()
        first_part, second_part = word[0:i], word[i:len(word)]

        if first_part in words:
            part['first'] = first_part
            if second_part in words:
                part['second'] = second_part
                # if the small words are both in the word list, add them to sub list
                # word is a composed word
                sub.append(part)

    return sub

def main():
    try:
        words = []
        with open("wordlist.txt") as file:
            words = filter(None, (line.rstrip() for line in file)) # Non-blank lines

        file.close()

        # get 6 letters words
        six_letters_words = filter_words(words)

        # get words whose length is smaller than MAX_LENGTH
        other_words = [word for word in words if len(word) < MAX_LENGTH]  # use list comprehension

        index = 0
        nb_of_composed_words = 0
        # for each word, check if it that word is composed of two concatenated smaller words
        for word in six_letters_words:
            index += 1
            sub = is_composed_of_sub_words(word, other_words)
            if sub:
                print sub
                nb_of_composed_words += 1
            print "progress %d %s" % ((index / len(six_letters_words)) * 100 , "%")

        print "%d word(s) are composed of smaller words" % nb_of_composed_words
    except Exception as e:
        print e

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Finished after %s seconds" % (time.time() - start_time))
