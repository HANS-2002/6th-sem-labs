# Define a class complex with required attributes and member functions and add two complex number and display the result
class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return complex(self.real+other.real, self.imag+other.imag)

    def __str__(self):
        return "({}+{}i)".format(self.real, self.imag)


c1 = complex(int(input('Real part of 1st complex number: ')),
             int(input('Imaginary part of 1st complex number: ')))
c2 = complex(int(input('Real part of 2nd complex number: ')),
             int(input('Imaginary part of 2nd complex number: ')))
c3 = c1+c2
print(f'Sum of {c1} and {c2} is {c3}')
