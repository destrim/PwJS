import random
import numpy as np


def matrixDet(matrix):
    if len(matrix[0]) == len(matrix):
        return np.linalg.det(matrix)
    else:
        return print("Matrix is not square.")


def main():
    n = random.randint(0, 100)
    matrix = [[random.randint(0, 100) for x in range(n)] for y in range(n)]
    matrix_det = matrixDet(matrix)
    print(matrix_det)


if __name__ == '__main__':
    main()
