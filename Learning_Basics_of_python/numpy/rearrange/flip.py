import numpy as np;
arr_1D=np.arange(0,6,1).flatten();
print("-------------------------------flip 1-D, axis-0--------------------------------------------")
print("Sample:\n",arr_1D);
flip_arr_1D=np.flip(arr_1D);
print("Original:\n",flip_arr_1D);
print("--------------------------------flip 2-D axis-0-----------------------------------------------------")
arr_2D=np.arange(0,9,1).reshape(3,3);
print("Sample:\n",arr_2D);
flip_arr_2D_axis_0=np.flip(arr_2D,axis=0);
print("Original:\n",flip_arr_2D_axis_0);
print("--------------------------------flip 2-D axis-1-----------------------------------------------------")
flip_arr_2D_axis_one=np.flip(arr_2D,axis=1);
print("Sample:\n",arr_2D);
print("Original:\n",flip_arr_2D_axis_one);
print("--------------------------------flip 3-D axis-0-----------------------------------------------------")
arr_3D=np.arange(100,370,10).reshape(3,3,3);
print("Sample:\n",arr_3D);
flip_arr_3D_axis_0=np.flip(arr_3D,axis=0);
print("Originl:\n",flip_arr_3D_axis_0);
print("--------------------------------flip 3-D axis-1-----------------------------------------------------")
print("Sample:\n",arr_3D);
flip_arr_3D_axis_1=np.flip(arr_3D,axis=1);
print("Original:\n",flip_arr_3D_axis_1);
print("--------------------------------flip 3-D axis-2-----------------------------------------------------")
print("Sample:\n",arr_3D);
flip_arr_3D_axis_2=np.flip(arr_3D,axis=2);
print("Original:\n",flip_arr_3D_axis_2);
