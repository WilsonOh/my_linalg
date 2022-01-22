import rref_solver
# import numpy as np

a = [
        [1, 2, 3, 4],
        [0, 1, 2, 3],
        [0, 0, 2, 2]
        ]


print(rref_solver.rref(a))
rref_solver.show_ans(a)
