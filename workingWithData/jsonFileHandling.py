import json
import os


def openJSON(path):
    if os.path.isfile(path):
        with open(path, "r") as file:
            return json.load(file)
    else:
        return []


def saveJSON(data, path):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)


def printData(data):
    for a in range(0, len(data)):
        print("\nNo. " + str(a+1))
        print("name:", data[a]["name"])
        print("description:", data[a]["description"])
        print("date:", data[a]["date"])


def addNote():
    print()
    name = input("\t" + "name: ")
    des = input("\t" + "description: ")
    date = input("\t" + "date: ")

    note = {"name": name, "description": des, "date": date}
    return note


def removeNote():
    print()
    n = int(input("\t" + "Which one u want to remove?: "))
    return n-1


def main():

    path = "files/data_file.json"
    data = openJSON(path)

    while(True):
        printData(data)
        print("\n" + "What u want to do: ")
        print("\t" + "1. Add note")
        print("\t" + "2. Remove note")
        print("\t" + "0. Exit")
        choice = int(input("Choose number: "))
        if choice == 1:
            data.append(addNote())
        elif choice == 2:
            data.pop(removeNote())
        elif choice == 0:
            break

    saveJSON(data, path)


if __name__ == '__main__':
    main()
