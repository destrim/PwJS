import random


def bubbleSort(tab):
    n = len(tab)
    for i in range(0, n-1):
        for j in range(1, n-i):
            if tab[j-1] > tab[j]:
                tmp = tab[j]
                tab[j] = tab[j-1]
                tab[j-1] = tmp
    return tab


def main():
    random_tab = []
    for i in range(0, 50):
        random_tab.append(random.randint(0, 100))

    print(random_tab)

    bubblesort_tab = bubbleSort(random_tab)
    random_tab.sort()

    print(bubblesort_tab)
    print(random_tab)


if __name__ == '__main__':
    main()
