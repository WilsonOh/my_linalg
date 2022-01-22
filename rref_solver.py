import numpy as np


# Defined 2D list as matrix to make type hints cleaner
matrix = list[list[float]]


class InconsistentMatrixError(ValueError):
    """Custom exception which is raised when the system of equations
       in the augmented matrix is inconsistent"""

    def __init__(self, row, idx):
        super().__init__(f"row {idx + 1}: {row} is inconsistent.")


def check_consistency(m: matrix):
    """Checks for the consistency of the system of equations
        in an augmented matrix"""
    m = np.array(m)
    for idx, row in enumerate(m[:, : len(m[0]) - 1]):
        if (sum(row) != 0) == 0:
            raise InconsistentMatrixError(m[idx], idx)


def rref(m: matrix) -> matrix:
    """Finds the Reduced Row Echelon Form of an augmented matrix"""
    # First find the REF of the matrix
    m = ref(m)

    # for each entry after the leading entry, subtract by
    # a multiple of the row below to make all entries in
    # the pivot row besides the leading entry 0
    for idx, row in enumerate(m):
        for i in range(idx + 1, len(m)):
            n = m[i][i]
            if n != 0:
                mul = row[i]/n
                for item_idx, item in enumerate(row):
                    m[idx][item_idx] -= mul * m[i][item_idx]
    return m


def ref(m: matrix) -> matrix:
    """Finds the Row Echelon Form of an augmented matrix"""

    # check for consistency before attempting to solve
    check_consistency(m)
    m = np.array(m, dtype=float)

    # Following the gaussian algo, swap the first row with another
    # row that has a non-zero entry in the leftmost column if needed
    for idx, n in enumerate(m[:, 0]):
        if n != 0:
            m[[0, idx]] = m[[idx, 0]]
            break

    # For each row, add a suitable multiple of the row above
    # to make entries below the leading entry of each row 0
    for idx, row in enumerate(m):
        for i in range(idx):
            if row[i] != 0:
                mul = row[i]/m[i][i]
                for j in range(len(row)):
                    m[idx][j] -= mul * m[i][j]

        div = row[idx]
        # Divide each row by the leading entry to make the leading entry 1
        if div != 0:
            for item_idx, item in enumerate(row[:]):
                m[idx][item_idx] /= div

    return m


def show_ans(m: matrix) -> None:
    """Finds the RREF of an augmented matrix and prints out
       it's unique solutions"""
    m = rref(ref(m))
    for idx, row in enumerate(m):
        print(f"x{idx + 1} = {(row[-1]):.2f}")
