import numpy as np
signal = np.array([1, 3, 5, 7])
kernel = np.array([1, 2, 3])
get_con=np.convolve(signal, kernel, mode="valid")
print(get_con)