import random


def matrixGen(matrix_x, matrix_y):
    matrix = [[random.randint(0, 100) for x in range(matrix_x)] for y in range(matrix_y)]
    return matrix


def matrixSum(matrix1, matrix2):
    matrix_x = len(matrix1[0])
    matrix_y = len(matrix1)
    matrix = [[0 for x in range(matrix_x)] for y in range(matrix_y)]

    if matrix_x == len(matrix2[0]) and matrix_y == len(matrix2):
        for i in range(0, matrix_x):
            for j in range(0, matrix_y):
                matrix[i][j] = matrix1[i][j] + matrix2[i][j]

    return matrix


def main():
    matrix1 = matrixGen(128, 128)
    matrix2 = matrixGen(128, 128)

    matrix3 = matrixSum(matrix1, matrix2)


if __name__ == '__main__':
    main()
