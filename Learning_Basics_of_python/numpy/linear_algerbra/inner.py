import numpy as np;
arr001=np.arange(0,18,1).reshape(2,3,3);
print("Arr001:\n",arr001);
arr002=np.arange(100,280,10).reshape(2,3,3);
print("Arr002:\n",arr002);
print("-------------------------------Inner 3D-----------------------------------------")
make_inner=np.inner(arr001,arr002);
print("Inner Product:\n",make_inner);
print("-------------------------------Inner 2D-----------------------------------------")
arr_2D_001=np.arange(0,9,1).reshape(3,3);
arr_2D_002=np.arange(10,19,1).reshape(3,3);
print("arr_2D_001:\n",arr_2D_001);
print("arr_2D_002:\n",arr_2D_002);
make_inner_2D=np.inner(arr_2D_001,arr_2D_002);
print("Inner:\n",make_inner_2D);