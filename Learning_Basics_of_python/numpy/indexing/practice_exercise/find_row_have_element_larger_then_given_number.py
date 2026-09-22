import numpy as np
arr = np.array([[1, 5], [7, 2], [3, 9]])
num=6;
new_arr=np.where(np.any(arr>num,axis=1))
print("New Array:\n",new_arr);