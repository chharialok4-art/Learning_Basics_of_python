import numpy as np
A = np.array([
    [1, 1, 1],
    [2, 1, 1],
    [1, 2, 1]
])
B = np.array([6, 7, 8])
X = np.linalg.solve(A, B)
print("Solve:\n",X)