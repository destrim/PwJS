import os


def main():
    path = "/dev"  # it will work on Linux, but not on Windows
    print(len(os.listdir(path)))


if __name__ == '__main__':
    main()
