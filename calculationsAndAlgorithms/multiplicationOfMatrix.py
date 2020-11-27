import random


def matrixMulti(matrix1, matrix2):
    a = len(matrix1)
    b = len(matrix2[0])

    matrix_res = [[0 for x in range(b)] for y in range(a)]

    if len(matrix1[0]) == len(matrix2):
        for i in range(0, a):
            for j in range(0, b):
                for k in range(0, len(matrix1[0])):
                    matrix_res[j][i] += matrix1[j][k] * matrix2[k][i]

    return matrix_res


def main():
    matrix1 = [[random.randint(0, 100) for x in range(8)] for y in range(8)]
    matrix2 = [[random.randint(0, 100) for x in range(8)] for y in range(8)]
    matrix3 = matrixMulti(matrix1, matrix2)

    print(matrix3)


if __name__ == '__main__':
    main()
