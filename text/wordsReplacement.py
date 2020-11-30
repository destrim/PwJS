
def main():
    replacement = {
        "i": "oraz",
        "oraz": "i",
        "nigdy": "prawie nigdy",
        "dlaczego": "czemu"
    }

    text = open('words.txt', 'r')
    text_string = text.read()
    text.close()

    print(text_string)

    text_string = text_string.replace(".", " .")
    text_string = text_string.replace(",", " ,")
    text_string = text_string.split()

    for i in range(0, len(text_string)):
        for x in replacement:
            if text_string[i] == x:
                text_string[i] = replacement[x]
                break

    text_string = " ".join(text_string)

    print(text_string)


if __name__ == '__main__':
    main()
