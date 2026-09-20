import numpy as np;
arr_2D=np.arange(0,9,1).reshape(3,3);
print("Original:\n",arr_2D);
print("---------------------------------mean 2D array---------------------------------------------")
mean_2D_axis_zero=np.mean(arr_2D,axis=0);
print("mean_2D_axis_zero:\n",mean_2D_axis_zero);
mean_2D_axis_one=np.mean(arr_2D,axis=1);
print("mean_2D_axis_one:\n",mean_2D_axis_one);
print("---------------------------------mean 3D array---------------------------------------------")
arr_3D=np.arange(0,18,1).reshape(2,3,3);
print("Original:\n",arr_3D);
mean_3D_axis_zero=np.mean(arr_3D,axis=0);
print("mean_3D_axis_zero:\n",mean_3D_axis_zero);
mean_3D_axis_one=np.mean(arr_3D,axis=1);
print("mean_3D_axis_one:\n",mean_3D_axis_one);
mean_3D_axis_two=np.mean(arr_3D,axis=2);
print("mean_3D_axis_two:\n",mean_3D_axis_two);