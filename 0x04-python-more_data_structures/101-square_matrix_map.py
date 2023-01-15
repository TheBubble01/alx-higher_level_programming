#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda mem: list(map(lambda elem: elem * elem, mem)), matrix))
