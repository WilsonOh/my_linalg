import rref_solver

a = [
        [3, 2, -4, 3],
        [2, 3, 3, 15],
        [5, -3, 1, 14]
        ]

# Answer should be x1 = 3, x2 = 1, x3 = 2


print(rref_solver.rref(a))
rref_solver.show_ans(a)
