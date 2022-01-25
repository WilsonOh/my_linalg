import rref_solver
import numpy as np
# import sympy as sym

# a = [
#         [3, 2, -4, 3],
#         [2, 3, 3, 15],
#         [5, -3, 1, 14]
#         ]

a = [
        [1, 0, -1, 0],
        [4, 0, 0, -2],
        [0, 2, -2, -1]
        ]

b = [
        [3, 5],
        [1, 2]
        ]

print(rref_solver.inv(b))
print()
print(np.linalg.inv(b))

# Answer should be x1 = 3, x2 = 1, x3 = 2
# print(rref_solver.rref(a))
# print(sym.Matrix(C).rref())
# rref_solver.show_ans(a)
