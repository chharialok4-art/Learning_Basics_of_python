import numpy as np;
arr001=np.arange(0,9,1);
print("--------------------------------1D spliting---------------------------------------------------")
print("Creating Array:\n",arr001);
make_split=np.split(arr001,3);
print("Splited:\n",make_split);
for idx,arr in enumerate(make_split):
    print(idx,":",arr);
print("--------------------------------2D spliting Axis-0---------------------------------------------------")
arr_2D=np.arange(0,6,1).reshape(2,3);
print("arr_2D:\n",arr_2D);
print("\n");
make_split_2D_Axis_Zero=np.split(arr_2D,1,axis=0);
for idx,arr in enumerate(make_split_2D_Axis_Zero):
    print(idx,":\n",arr);
print("--------------------------------2D spliting Axis-1---------------------------------------------------")
make_split_2D_Axis_One=np.split(arr_2D,3,axis=1);
for idx,arr in enumerate(make_split_2D_Axis_One):
    print(idx,":\n",arr);
print("-----------------------------------------------------------------------------------")
arr_3D=np.arange(0,18,1).reshape(2,3,3);
print("3D array:\n",arr_3D);
print("--------------------------------3D spliting Axis-0---------------------------------------------------")
arr_3D_split_axis_zero=np.split(arr_3D,2,axis=0);
print("arr_3D_split_axis_zero:\n",arr_3D_split_axis_zero)
for idx,arr in enumerate(arr_3D_split_axis_zero):
    print(idx,":\n",arr);
print("--------------------------------3D spliting Axis-1 divide(3)---------------------------------------------------")
arr_3D_split_axis_one=np.split(arr_3D,3,axis=1);
print("arr_3D_split_axis_one:\n",arr_3D_split_axis_one)
for idx,arr in enumerate(arr_3D_split_axis_one):
    print(idx,":\n",arr);
print("------------------------------3D spliting Axis-1 divide(2)--------------------------------------------")
arr_3D_split_axis_ONE_divide_One=np.split(arr_3D,1,axis=1);
print("arr_3D_split_axis_one:\n",arr_3D_split_axis_ONE_divide_One)
for idx,arr in enumerate(arr_3D_split_axis_ONE_divide_One):
    print(idx,":\n",arr);
print("--------------------------------3D spliting Axis-2 Divide-3------------------------------------------------")
arr_3D_split_axis_two_divide_three=np.split(arr_3D,3,axis=2);
for idx,arr in enumerate(arr_3D_split_axis_two_divide_three):
    print(idx,":\n",arr)
print("--------------------------------3D spliting Axis-2 Divide-1------------------------------------------------")
arr_3D_split_axis_two_divide_one=np.split(arr_3D,1,axis=2);
for idx,arr in enumerate(arr_3D_split_axis_two_divide_one):
    print(idx,":\n",arr)