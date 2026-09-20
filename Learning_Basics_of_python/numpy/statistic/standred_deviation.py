import numpy as np;
print("----------------------------------2D array ---------------------------------------------")
ar_2D=np.arange(0,9,1).reshape(3,3);
print("Originsl:\n",ar_2D);
std_2D_axis_zero=np.std(ar_2D,axis=0);
print("std_2D_axis_zero:\n",std_2D_axis_zero);
std_2D_axis_one=np.std(ar_2D,axis=1);
print("std_2D_axis_one:\n",std_2D_axis_one);
print("----------------------------------3D array ---------------------------------------------")
ar_3D=np.arange(10,37,1).reshape(3,3,3);
print("Originsl:\n",ar_3D);
std_3D_axis_zero=np.std(ar_3D,axis=0);
print("std_3D_axis_zero:\n",std_3D_axis_zero);
std_3D_axis_one=np.std(ar_3D,axis=1);
print("std_3D_axis_one:\n",std_3D_axis_one);
std_3D_axis_two=np.std(ar_3D,axis=2);
print("std_3D_axis_one:\n",std_3D_axis_two);