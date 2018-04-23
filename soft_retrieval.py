import string
import json


def check_in_unigrams(term):

    dict_read = open('C:/Users/Srivardhan/Desktop/NeU/IR/project/code/unigrams_tf.json')
    unigram_dict = json.load(dict_read)

    edit_dist_dict = {}

    for i in unigram_dict:
        if i[0] == term[0] and i[len(i) - 1] == term[len(term) - 1] and len(i) == len(term):
            edit_dist_dict[i] = edit_distance(term, i, len(term), len(i))

    best_dist = 100

    for i in edit_dist_dict:
        if best_dist > edit_dist_dict[i]:
            best_dist = edit_dist_dict[i]

    best_words = []

    for i in edit_dist_dict:
        if edit_dist_dict[i] is best_dist:
            best_words.append(i)

    best_words_tf = []

    for i in best_words:
        best_words_tf.append(unigram_dict[i])

    if len(best_words_tf) > 0:
        max_tf = max(best_words_tf)

    for i in range(0, len(best_words_tf)):
        if max_tf == best_words_tf[i]:
            return best_words[i]

    return term


def edit_distance(term, unigram, term_len, term_unigram):

    if term_len == 0:
        return term_unigram

    if term_unigram == 0:
        return term_len

    if term[term_len - 1] == unigram[term_unigram - 1]:
        return edit_distance(term, unigram, term_len - 1, term_unigram - 1)

    return min(edit_distance(term, unigram, term_len, term_unigram - 1),  # Insert
               edit_distance(term, unigram, term_len - 1, term_unigram),  # Remove
               edit_distance(term, unigram, term_len - 1, term_unigram - 1)  # Replace
               ) + 1


def _soft_noise_remover_():

    inp = raw_input("Please enter the query\n")

    best_suggestion = check_in_unigrams(inp.lower())

    if best_suggestion != inp.lower():
        print('Searching for term: ' + best_suggestion)
    else:
        print('No suggestion found for the term. Ranking using the same term instead: ' + best_suggestion)


_soft_noise_remover_()
