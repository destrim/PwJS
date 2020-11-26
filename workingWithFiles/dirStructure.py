import os


def dirTree(path):
    print("\n" + path)
    print(os.listdir(path))
    prev_path = os.path.dirname(path)
    if prev_path != path:
        dirTree(prev_path)


def main():
    path = r""  # here comes the path

    dirTree(path)


if __name__ == '__main__':
    main()
