import numpy as np;
arr001=np.arange(100,370,10).reshape(3,3,3);
print("Determinant 3D:\n",np.linalg.det(arr001));
arr002=np.arange(10,19,1).reshape(3,3);
print("determinant 2D:\n",np.linalg.det(arr002));

