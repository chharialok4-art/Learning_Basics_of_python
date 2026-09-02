import numpy as np;
arr_1D=np.arange(0,10,1).reshape(1,10).flatten();
print("--------------------------------------1D Insert--------------------------------------------")
inserted_arr_1D=np.array([100,200,300]);
arr_1D=np.insert(arr_1D,4,inserted_arr_1D,axis=0);
print(arr_1D);
print("--------------------------------------2D Insert, axis-0-------------------------------------------")
arr_2D=np.arange(100,1000,100).reshape(3,3);
inserted_arr_2D=np.arange(101,104,1).reshape(1,3).flatten();
arr_2D=np.insert(arr_2D,3,inserted_arr_2D,axis=0);
print(arr_2D);
print("--------------------------------------2D Insert, axis-1-------------------------------------------")
inserted_arr_2D_axis_1=np.arange(104,108,1).reshape(4,1).flatten();
arr_2D=np.insert(arr_2D, 3, inserted_arr_2D_axis_1, axis=1);
print(arr_2D);
print("--------------------------------------3D Insert, axis-0-------------------------------------------")
arr_3D=np.arange(0,2700,100).reshape(3,3,3);
inserted_arr_3D_axis_0=np.arange(0,9,1).reshape(3,3);
arr_3D=np.insert(arr_3D,1,inserted_arr_3D_axis_0,axis=0);
print(arr_3D);
print("--------------------------------------3D Insert, axis-1-------------------------------------------")
inserted_arr_3D_axis_1=np.arange(101,113,1).reshape(4,3);
arr_3D=np.insert(arr_3D,3,inserted_arr_3D_axis_1,axis=1);
print(arr_3D);
print("--------------------------------------3D Insert, axis-2-------------------------------------------")
inserted_arr_3D_axis_2=np.arange(1000,1016,1).reshape(4,4);
arr_3D=np.insert(arr_3D,3,inserted_arr_3D_axis_2,axis=2);
print(arr_3D);