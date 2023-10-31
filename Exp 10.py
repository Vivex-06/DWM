import numpy as np
from fractions import Fraction

def display_format(my_vector, my_decimal):
    return np.round(my_vector.astype(float), decimals=my_decimal)

my_dp = Fraction(1, 3)
Mat = np.matrix([[0, 0, 1],
                [Fraction(1, 2), 0, 0],
                [Fraction(1, 2), 0, 0]])
Ex = np.zeros((3, 3))
Ex[:] = my_dp

beta = 0.7
A1 = beta * Mat + ((1 - beta) * Ex)

r = np.matrix([my_dp, my_dp, my_dp])
r = np.transpose(r)
previous_r = r

for i in range(1, 100):
    r = A1 * r
    if (previous_r == r).all():
        break
    previous_r = r

print("Final:\n", display_format(r, 3))
print("Sum:", np.sum(r))
