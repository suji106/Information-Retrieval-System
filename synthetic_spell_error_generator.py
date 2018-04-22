import random


def synthetic_spell_error_generator(query):

    print query
    query_terms = query.split()

    query_errored = []
    for i in query_terms:
        query_errored.append(i)

    error_ratio = int(0.4 * float(len(query_terms)))
    error_terms = random.randint(0, error_ratio)

    query_terms_lens = []
    for i in range(0, len(query_terms)):
        query_terms_lens.append(len(query_terms[i]))

    error_indexes = []

    for i in range(0, error_terms):

        big_words_prob = random.randint(0, 100)          # 70% probability for bigger words. 30% for all the words

        if big_words_prob < 70:
            max_val = max(query_terms_lens)
            for e in range(0, len(query_terms_lens) - 1):
                if query_terms_lens[e] is max_val:
                    query_terms_lens[e] = 0
                    error_indexes.append(e)
                    break
        else:
            while 1 > 0:
                num = random.randint(0, len(query_terms_lens) - 1)
                if len(query_terms[num]) > 3 and num not in error_indexes:
                    error_indexes.append(num)
                    break

    error_indexes = sorted(error_indexes)

    for i in error_indexes:
        term = query_terms[i]
        change = []
        change_num = random.randint(2, len(term) - 2)
        if change_num % 2 is 1:
            change_num += 1
        if change_num >= len(term) - 1:
            change_num -= 2

        for j in range(0, change_num):
            while len(term) >= 4:
                rand_num = random.randint(1, len(term) - 2)
                if rand_num not in change:
                    change.append(rand_num)
                    break

        for index in range(0, len(change) - 1, 2):
            temp = term[change[index]]
            term = term[0:change[index]] + term[change[index + 1]] + term[change[index] + 1:]
            term = term[0:change[index + 1]] + temp + term[change[index + 1] + 1:]

        query_errored[i] = term

    query_with_errors = ''

    for i in query_errored:
        query_with_errors += i + ' '
    query_with_errors = query_with_errors[: -1]

    print query_with_errors


synthetic_spell_error_generator('This would be very difficult word enjoying itself. One of the biggest problems of taking information retrieval would be studying without breaks')
