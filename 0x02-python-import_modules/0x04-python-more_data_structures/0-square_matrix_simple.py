#!/usr/bin/python3
"""
wordA function that computes the square
value of all integers of a matrix.
"""
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for col in matrix:
        result = list(lambda x**2, col)
        new_matrix.append(result)
    return(new_matrix)
