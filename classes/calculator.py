from classes import complexNumbers as cN


def main():
    inputstr = input("Write equation, separating each character by space: ").split(' ')
    num1 = cN.ComplexNum(int(inputstr[0]), int(inputstr[2]))
    num2 = cN.ComplexNum(int(inputstr[5]), int(inputstr[7]))
    res = cN.ComplexNum(0, 0)
    operation = inputstr[4]

    if operation == '+':
        res = num1 + num2
    elif operation == '-':
        res = num1 - num2
    elif operation == '*':
        res = num1 * num2
    else:
        print("Wrong operation.")

    print(res.print())


if __name__ == '__main__':
    main()
