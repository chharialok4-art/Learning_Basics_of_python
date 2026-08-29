import numpy as np;
arr_3D=np.arange(0,45,1).reshape(5,3,3);
print("----------------------------------3D-dsplit divide(3)------------------------------------------------")
dsplit_3D_divide_three=np.dsplit(arr_3D,3);
for idx,arr in enumerate(dsplit_3D_divide_three):
    print(idx,":\n",arr);
