#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for li in matrix:
            for item in li:
                print("{:d}".format(item), end=" " if item != li[-1] else "\n")

    else:
        print()
