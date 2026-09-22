import numpy as np;
arr = np.array([1, 10, 2, 0, 3, 9, 0, 5, 0, 7, 5, 0, 0]);
get_idx=np.where(arr==0)
print("Index:\n",get_idx);