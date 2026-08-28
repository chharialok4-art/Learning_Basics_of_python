import numpy as np;
arr_1D=np.arange(100,260,10).reshape(4,4);
print("Original Array:\n",arr_1D);
print("--------------------------------hSplit-2D-Divide(2)------------------------------------------")
arr_2D_hsplit_divide_two_parts=np.hsplit(arr_1D,2);
for idx,arr in enumerate(arr_2D_hsplit_divide_two_parts):
    print(idx,":\n",arr);
print("--------------------------------hSplit-2D-Divide(4)------------------------------------------")
arr_2D_hsplit_divide_four_parts=np.hsplit(arr_1D,4);
for idx,arr in enumerate(arr_2D_hsplit_divide_four_parts):
    print(idx,":\n",arr);
NOTE= "This 2D array cannot be divided into 3 parts";
