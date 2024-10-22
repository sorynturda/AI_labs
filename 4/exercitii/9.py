class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag*other.imag,
                       self.real * other.imag + self.imag * other.real)

    def __str__(self):
        return f'{self.real} + {self.imag}j'


no1 = Complex(3, 2)
no2 = Complex(5, 6)
print(no1 + no2)
print(no1 - no2)
print(no1 * no2)
