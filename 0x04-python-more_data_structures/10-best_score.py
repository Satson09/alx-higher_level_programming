#!/usr/bin/python3
def best_score(a_dictionary):
    """
    A function that returns a key with the biggest integer value.
    """
    if not a_dictionary:
        return(none)
    one_loop = True
    for people in a_dictionary:
        if one_loop:
            best = people
            score = a_dictionary[people]
            one_loop = False
        if a_dictionary[people] > score:
             score = a_dictionary[people]
             best = people
        return(best)
