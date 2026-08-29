import numpy as np;
arr_1D=np.arange(0,10,1).reshape(1,-1);
print("-----------------------------------vsplit 1D divide(1)-------------------------------------------")
vsplit_1D=np.vsplit(arr_1D,1);
print("vsplit_1D:\n",vsplit_1D);
print("-----------------------------------vsplit 2D divide(4)-------------------------------------------")
arr_2D=np.arange(0,100,5).reshape(4,5);
vsplit_2D=np.vsplit(arr_2D,4);
for idx,arr in enumerate(vsplit_2D):
    print(idx,":",arr);
print("-----------------------------------vsplit 2D divide(2)-------------------------------------------")
vsplit_2D_divide_two=np.vsplit(arr_2D,2);
for idx,arr in enumerate(vsplit_2D_divide_two):
    print(idx,":\n",arr);
print("-----------------------------------vsplit 3D divide(2)-------------------------------------------")
arr_3D=np.arange(0,36,1).reshape(4,3,3);
vsplit_3D_divide_2=np.vsplit(arr_3D,2);
for idx,arr in enumerate(vsplit_3D_divide_2):
    print(idx,":\n",arr);
print("-----------------------------------vsplit 3D divide(4)-------------------------------------------")
arr_3D=np.arange(0,36,1).reshape(4,3,3);
vsplit_3D_divide_4=np.vsplit(arr_3D,4);
for idx,arr in enumerate(vsplit_3D_divide_4):
    print(idx,":\n",arr);