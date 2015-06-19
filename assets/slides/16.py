def str_repr_demos():
    from datetime import date
    today = date(2014, 10, 13)
    today
    print(today)

    s = 'hello world'
    str(s)
    repr(s)
    "'hello world'"
    repr(repr(repr(s)))
    eval(eval(eval(repr(repr(repr(s))))))
    # Errors: eval('hello world')

# Implementing generic string functions

class Bear:
    """A Bear."""
    def __init__(self):
        self.__repr__ = lambda: 'oski'
        self.__str__ = lambda: 'oski the bear'

    def __repr__(self):
        return 'Bear()'

    def __str__(self):
        return 'a bear'

def print_bear():
    oski = Bear()
    print(oski)
    print(str(oski))
    print(repr(oski))
    print(oski.__repr__())
    print(oski.__str__())

def repr(x):
    return type(x).__repr__(x)

def str(x):
    t = type(x)
    if hasattr(t, '__str__'):
        return t.__str__(x)
    else:
        return repr(x)

# Rational numbers

class Rational:
    """A mutable fraction.

    >>> f = Rational(3, 5)
    >>> f
    Rational(3, 5)
    >>> print(f)
    3/5
    >>> f.float_value
    0.6
    >>> f.numer = 4
    >>> f.float_value
    0.8
    >>> f.denom -= 3
    >>> f.float_value
    2.0
    """
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numer, self.denom)

    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)

    @property
    def float_value(self):
        return self.numer/self.denom

# Complex numbers

from math import atan2, sin, cos, pi

class Complex:
    def add(self, other):
        return ComplexRI(self.real + other.real, 
                         self.imag + other.imag)

    def mul(self, other):
        return ComplexMA(self.magnitude * other.magnitude, 
                         self.angle + other.angle)

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.mul(other)

class ComplexRI(Complex):
    """A rectangular representation of a complex number.

    >>> from math import pi
    >>> ComplexRI(1, 2).add(ComplexMA(2, pi/2))
    ComplexRI(1, 4)
    >>> ComplexRI(0, 1).mul(ComplexRI(0, 1))
    ComplexMA(1, 1 * pi)
    >>> ComplexRI(1, 2) + ComplexMA(2, 0)
    ComplexRI(3, 2)
    >>> ComplexRI(0, 1) * ComplexRI(0, 1)
    ComplexMA(1, 1 * pi)
    """
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    @property
    def angle(self):
        return atan2(self.imag, self.real)

    def __repr__(self):
        return 'ComplexRI({0:g}, {1:g})'.format(self.real, self.imag)

class ComplexMA(Complex):
    """A polar representation of a complex number."""
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle

    @property
    def real(self):
        return self.magnitude * cos(self.angle)

    @property
    def imag(self):
        return self.magnitude * sin(self.angle)

    def __repr__(self):
        return 'ComplexMA({0:g}, {1:g} * pi)'.format(self.magnitude, 
                                                     self.angle/pi)
