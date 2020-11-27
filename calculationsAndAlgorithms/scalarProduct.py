
def scalar(a, b):
    i = len(a)
    j = len(b)

    aob = 0
    if i == j:
        for n in range(0, i):
            aob += (a[n] * b[n])

    return aob


def main():
    a = [1, 2, 12, 4]
    b = [2, 4, 2, 8]

    print(scalar(a, b))


if __name__ == '__main__':
    main()
