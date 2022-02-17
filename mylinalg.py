import numpy as np
from numpy.typing import NDArray


class InconsistentMatrixError(ValueError):
    """Custom exception which is raised when the system of equations
       in the augmented matrix is inconsistent"""

    def __init__(self, row, idx):
        super().__init__(f"row {idx + 1}: {row} is inconsistent.")


def matmul_alt(a: NDArray, b: NDArray) -> NDArray:
    """matrix multiplication implementation in pure python"""
    if len(a[0]) != len(b):
        raise ValueError("Invalid dimensions for matrix multiplication")
    return np.array([[sum([a[k][j] * b[j][i] for j in range(len(b))])
                      for i in range(len(b[0]))] for k in range(len(a))])


def matmul(m: NDArray, n: NDArray) -> NDArray:
    """faster and more efficient method using numpy arrays. Though at this
       point you should just use np.matmul"""
    if len(m[0]) != len(n):
        raise ValueError("Invalid dimensions for NDArray multiplication")
    return np.array([[np.dot(row, col) for col in n.T] for row in m])


def det(m: NDArray) -> float:
    row, col = m.shape
    if row != col:
        raise ValueError("Not a square NDArray")
    if len(m) == 1:
        return m[0][0]
    if len(m) == 2:
        return (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
    res = 0
    for idx, entry in enumerate(m[0]):
        minor = np.delete(np.delete(m, 0, 0), idx, 1)
        res += entry * (-1)**idx * det(minor)
    return res


def vander(m: list[int], N=None, increasing=False) -> NDArray:
    vander_monde = []
    if N is None:
        N = len(m)
    if increasing:
        for i in m:
            vander_monde.append([i**x for x in range(N)])
    else:
        for i in m:
            vander_monde.append([i**x for x in range(N - 1, -1, -1)])
    return np.array(vander_monde)


def check_trivial(m: NDArray) -> bool:
    return True if sum(m[:, -1]) == 0 else False


def is_unique(m: NDArray) -> bool:
    for row in m[:, : len(m[0]) - 1]:
        if (sum(row != 0)) > 1:
            return False
    return True


def check_consistency(m: NDArray):
    """Checks for the consistency of the system of equations
        in an augmented NDArray"""
    m = np.array(m)
    for idx, row in enumerate(m[:, : len(m[0]) - 1]):
        if sum(row != 0) == 0:
            raise InconsistentMatrixError(m[idx], idx)


def rref(m: NDArray) -> NDArray:
    """Finds the Reduced Row Echelon Form of an augmented NDArray"""
    # First find the REF of the NDArray
    m = ref(m)

    # for each entry after the leading entry, subtract by
    # a multiple of the row below to make all entries in
    # the pivot row besides the leading entry 0
    for idx, row in enumerate(m):
        for i in range(idx + 1, len(m)):
            n = m[i][i]
            if n != 0:
                mul = row[i]/n
                for item_idx, _ in enumerate(row):
                    m[idx][item_idx] -= mul * m[i][item_idx]
    return m


def ref(m: NDArray) -> NDArray:
    """Finds the Row Echelon Form of an augmented NDArray"""

    # check for consistency before attempting to solve
    check_consistency(m)

    # Following the gaussian algo, swap the first row with another
    # row that has a non-zero entry in the leftmost column if needed
    for idx, n in enumerate(m[:, 0][0:]):
        if n != 0:
            m[[0, idx]] = m[[idx, 0]]
            break

    # For each row, add a suitable multiple of the row above
    # to make entries below the leading entry of each row 0
    for idx, row in enumerate(m):
        for i in range(idx):
            if row[i] != 0:
                n = m[i][i]
                if n != 0:
                    mul = row[i]/n
                    for j in range(len(row)):
                        m[idx][j] -= mul * m[i][j]

        div = row[idx]
        # Divide each row by the leading entry to make the leading entry 1
        if div != 0:
            for item_idx, _ in enumerate(row[:]):
                m[idx][item_idx] /= div

    check_consistency(m)
    return m


def eye(order: int) -> NDArray:
    return np.array([[1 if i == j else 0 for i in range(order)]
                     for j in range(order)])


def inv(m: NDArray):
    order = len(m)
    identity = eye(order)
    block = np.hstack((m, identity))
    return rref(block)[:, order:]


def print_aug_NDArray(m: NDArray):
    for row in m:
        width = max(list(map(len, map(str, row))))
        for idx, elem in enumerate(row):
            diff = len(str(elem)) - width
            if idx == len(row) - 1:
                print('|', end=' ')
            print((diff) * ' ', end='')
            print(elem, end=' ')
        print()


def show_ans(m: NDArray) -> None:
    """Finds the RREF of an augmented NDArray and prints out
       it's unique solutions"""
    m = rref(ref(m))
    if is_unique(m):
        for idx, row in enumerate(m):
            print(f"x{idx + 1} = {(row[-1]):.2f}")
    else:
        print("There are no unique solutions")
    if check_trivial(m) and is_unique(m):
        print("Trivial Solution")
