from fractions import Fraction
f1 = Fraction(3,4)
print(f1)
print(f1.numerator)
print(f1.denominator)
print(float(f1))
f2 = Fraction(7,8)
print(f2)
f3 = f1.__add__(f2)
f3= f1+f2
f4 = f3.__mul__(f2)
print(f4)
f5 = f2.__gt__(f4)
print(f5)
f6 = f1.__neg__()
print(f6)
f7= f1.__eq__(f2)
print(f7)

