#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    A function that adds all unique
    integers in a list (only once for each integer)
    """
    setlist = set(my_list)
    x = 0
    for i in setlist:
        x += i
    return (x)

