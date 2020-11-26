from PIL import Image
import os


def convertToPng(path):
    images = os.listdir(path)

    for a in images:
        a_path = os.path.join(path, a)
        if os.path.isfile(a_path):
            image = Image.open(a_path)
            a_path = a_path.replace('.jpg', '_PNG.png')
            image.save(a_path)


def main():
    path = "images\\"
    convertToPng(path)


if __name__ == '__main__':
    main()
