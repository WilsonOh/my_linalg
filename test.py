# import matplotlib.pyplot as plt
import numpy as np
# import sympy as sym
from numpy.polynomial.polynomial import Polynomial

# import rref_solver as rs

# sample_num = 10000
# v = np.linspace(0, 1, sample_num).reshape(sample_num, 1)
# b = np.exp(-(v**2))
# A = np.vander(v.flatten(), increasing=True)
# ans = np.linalg.solve(A, b)
# p = Polynomial(ans.flatten())
# p = p.integ(lbnd=0)
# print(p(1))


def eye(n, dtype=float):
    return np.array(
            np.fromfunction(lambda i, j: i == j, (n, n), dtype=int),
            dtype=dtype)


print(eye(10, dtype=int))
print(np.eye(10, dtype=int))
