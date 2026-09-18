import numpy as np
arr = np.arange(24).reshape(2, 3, 4)
print("Array Shape:\n",arr.shape)
print("Original Array:\n",arr);
print("------------------------------------from position 0 to 1-----------------------------------------")
arr_zero_to_one=np.moveaxis(arr,0,1);
print("Array Zero to One:\n",arr_zero_to_one);
print("------------------------------------from position 0 to 2-----------------------------------------")
arr_zero_to_one=np.moveaxis(arr,0,2);
print("Array Zero to Two:\n",arr_zero_to_one);
print("------------------------------------from position 1 to 2-----------------------------------------")
arr_zero_to_one=np.moveaxis(arr,1,2);
print("Array One to Two:\n",arr_zero_to_one);