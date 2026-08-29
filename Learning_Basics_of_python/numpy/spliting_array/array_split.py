import numpy as np;
arr_1D=np.arange(0,10,1).reshape(1,-1);
print("----------------------------array_split 1D divide (4)--------------------------------------------")
array_split_1D_divide_four=np.array_split(arr_1D,4,axis=1);
for idx,arr in enumerate(array_split_1D_divide_four):
    print(idx,":",arr);
print("----------------------------array_split, axis-0, 2D ,divide(3)--------------------------------------------")
arr_2D=np.arange(0,20,1).reshape(5,4);
print(arr_2D);
print("----------------------------------------------------------------------------------------")
array_split_2D_aixs_zero=np.array_split(arr_2D,3,axis=0);
for idx,arr in enumerate(array_split_2D_aixs_zero):
    print(idx,":\n",arr);
print("----------------------------array_split, axis-1, 2D ,divide(3)--------------------------------------------")
array_split_3D_aixs_one=np.array_split(arr_2D,3,axis=1);
for idx,arr in enumerate(array_split_3D_aixs_one):
    print(idx,":\n",arr);
print("----------------------------array_split, 3D, axis-0, divide(2)--------------------------------------------")
arr_3D=np.arange(0,60,1).reshape(3,5,4);
array_split_3D_divide_2_aixs_zero=np.array_split(arr_3D,2,axis=0);
for idx,arr in enumerate(array_split_3D_divide_2_aixs_zero):
    print(idx,":\n",arr);
print("----------------------------array_split, 3D, axis-1, divide(2)--------------------------------------------")
array_split_1D_divide_2_aixs_one=np.array_split(arr_3D,2,axis=1);
for idx,arr in enumerate(array_split_1D_divide_2_aixs_one):
    print(idx,":\n",arr);
print("----------------------------array_split, 3D, axis-2, divide(2)--------------------------------------------")
array_split_1D_divide_2_aixs_two=np.array_split(arr_3D,2,axis=2);
for idx,arr in enumerate(array_split_1D_divide_2_aixs_two):
    print(idx,":\n",arr);
