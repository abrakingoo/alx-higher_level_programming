#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary:

        sorted_score = sorted(a_dictionary.values(), reverse=True)

        if sorted_score:
            max_score = sorted_score[0]

            for key, value in a_dictionary.items():
                if value == max_score:
                    return key

    else:
        return None
