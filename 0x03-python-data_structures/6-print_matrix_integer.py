#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix or not matrix[0]:
        return

    for row in matrix:
        for num in row:
            print("{:d}".format(num), end=" ")
        print()
