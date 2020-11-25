
def codelock(corr):
    code = int(input("Input code: "))
    while code != corr:
        print("Wrong code! Try again.")
        code = int(input("Input code: "))
    print("The code was correct!")


def main():
    codelock(1234)


if __name__ == "__main__":
    main()
