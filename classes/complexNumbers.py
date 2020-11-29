class ComplexNum:
    real = 0
    imag = 0

    def __init__(self, r, i):
        self.real = r
        self.imag = i

    def print(self):
        if self.imag >= 0:
            print(str(self.real) + "+" + str(self.imag) + "i")
        else:
            print(str(self.real) + str(self.imag) + "i")

    def __add__(self, other):
        return ComplexNum(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNum(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return ComplexNum((self.real * other.real) - (self.imag * other.imag), (self.real * other.imag) + (other.real * self.imag))


def main():
    pass


if __name__ == '__main__':
    main()
