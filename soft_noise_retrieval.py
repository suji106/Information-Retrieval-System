import string


def term_searcher(term):

    rank_using_term = 0

    if rank_using_term is 0:
        shuffled_terms = edit_distance(term)
        missing_terms = missing(term)
        single_letter_replaced_terms = single_letter_replaces(term)
        single_letter_inserted_terms = single_letter_insertion(term)

    # print shuffled_terms
    # print missing_terms
    # print single_letter_replaced_terms
    # print single_letter_inserted_terms
    # print total_terms
    # print len(total_terms)

    total_terms = list(set(shuffled_terms + missing_terms + single_letter_replaced_terms + single_letter_inserted_terms))

    results = check_in_unigrams(total_terms)      # most probable results closest to the wrongly spelt term

    for i in results:
        print 'Did you mean ' + i

    if len(results) is 0:
        print 'No search results found for: ' + term


def edit_distance(word):

    w = []
    for i in range(0, len(word)):

        new_word = word[0: i] + word[i + 1: len(word)]

        if i is 0:
            for k in string.ascii_lowercase:
                w.append(new_word[0: i + 1] + k + new_word[i + 1: len(new_word)])

        if i is len(word) - 1:
            for k in string.ascii_lowercase:
                w.append(new_word[0: i - 1] + k + new_word[i - 1: len(new_word)])

        if i is not 0 and i is not len(word) - 1:
            for k in string.ascii_lowercase:
                w.append(new_word[0: i - 1] + k + new_word[i - 1: len(new_word)])
                w.append(new_word[0: i + 1] + k + new_word[i + 1: len(new_word)])

    w = list(set(w))

    return w


def missing(word):

    w = []
    for i in range(0, len(word)):

        w.append(word[0: i] + word[i + 1: len(word)])

    w = list(set(w))

    return w


def single_letter_replaces(word):

    w = []

    for i in range(0, len(word)):
        for k in string.ascii_lowercase:
            w.append(word[0: i] + k + word[i + 1: len(word)])

    w = list(set(w))

    return w


def single_letter_insertion(word):

    w = []
    for i in range(0, len(word)):
        for k in string.ascii_lowercase:
            w.append(word[0: i + 1] + k + word[i + 1: len(word)])
    w = list(set(w))
    return w


def check_in_unigrams(terms):

    unigrams = open('C:/Users/Srivardhan/Desktop/NeU/IR/project/code/unigrams.txt', 'r').readlines()
    result = []

    for i in range(0, len(unigrams)):
        unigrams[i] = unigrams[i].split('\n')[0]

    for i in terms:
        if i in unigrams:
            result.append(i)

    return result


term_searcher('intelhnigent')
