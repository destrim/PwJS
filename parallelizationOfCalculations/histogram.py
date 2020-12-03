import matplotlib.pyplot as plt
import threading
import cv2 as cv
import time

start_time = time.time()


def histogram(img, i, histr):
    histr[i] = (cv.calcHist([img], [i], None, [256], [0, 256]))


def main():
    path = r'images\image.jpg'
    img = cv.imread(path)
    col = ('b', 'g', 'r')
    histr = [0, 0, 0]

    threads = list()
    for i in range(3):
        t = threading.Thread(target=histogram, args=(img, i, histr,))
        threads.append(t)
        t.start()

    for i, thread in enumerate(threads):
        thread.join()
        plt.plot(histr[i], color=col[i])

    plt.title("Histogram")
    plt.grid(True)
    plt.xlim([0, 256])
    plt.show()


if __name__ == '__main__':
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
