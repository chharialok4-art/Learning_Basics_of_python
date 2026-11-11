import numpy as np
import matplotlib.pyplot as plt

image = np.array([
    [10, 20, 30, 40],
    [20, 30, 40, 50],
    [30, 40, 50, 60],
    [40, 50, 60, 70]
])

# Apply 2D Fourier Transform
fft_result = np.fft.fft2(image)

print(fft_result)
print(fft_result.shape)
plt.plot(fft_result)
plt.show()