#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    newlist = list(matrix)
    for i in range(3):
        for j in range(3):
            newlist[i][j] **= 2
