import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(np.quantile(arr, 0))
print(np.quantile(arr, 0.25))
print(np.quantile(arr, 0.50))
print(np.quantile(arr, 0.75))
print(np.quantile(arr, 1))
print("------------------------------------3D-----------------------------------------")
arr = np.array([
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])
print("Original:\n",arr);
print("Quantile Axis Zero:\n",np.quantile(arr, 0.25, axis=0))
print("Quantile Axis One:\n",np.quantile(arr, 0.25, axis=1))
print("Quantile Axis Two:\n",np.quantile(arr, 0.25, axis=2))
