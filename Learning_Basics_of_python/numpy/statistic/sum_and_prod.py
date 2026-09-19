import numpy as np;
ar_2D=np.arange(0,9,1).reshape(3,3);
print("-----------------------------------have sum 2D Array---------------------------------------------")
print("Original:\n",ar_2D)
make_sum=np.sum(ar_2D,axis=0);
print("make Sum axis Zero",make_sum);
make_sum_axis_one=np.sum(ar_2D,axis=1);
print("make Sum axis One",make_sum_axis_one);
print("-----------------------------------have sum 3D Array---------------------------------------------")
ar_3D=np.arange(0,27,1).reshape(3,3,3);
print("Original:\n",ar_3D);
make_sum_axis_3D_axis_zero=np.sum(ar_3D,axis=0);
print("make_sum_axis_3D_axis_zero:\n",make_sum_axis_3D_axis_zero)
make_sum_axis_3D_axis_One=np.sum(ar_3D,axis=1);
print("make_sum_axis_3D_axis_zero:\n",make_sum_axis_3D_axis_One)
make_sum_axis_3D_axis_Two=np.sum(ar_3D,axis=0);
print("make_sum_axis_3D_axis_zero:\n",make_sum_axis_3D_axis_Two)
print("-----------------------------------have product 2D Array---------------------------------------------")
print("Original:\n",ar_2D)
make_sum=np.prod(ar_2D,axis=0);
print("make Sum axis Zero",make_sum);
make_sum_axis_one=np.prod(ar_2D,axis=1);
print("make Sum axis One",make_sum_axis_one);
print("-----------------------------------have product 3D Array---------------------------------------------")
ar_3D=np.arange(0,27,1).reshape(3,3,3);
print("Original:\n",ar_3D);
make_sum_axis_3D_axis_zero=np.prod(ar_3D,axis=0);
print("make_sum_axis_3D_axis_zero:\n",make_sum_axis_3D_axis_zero)
make_sum_axis_3D_axis_One=np.prod(ar_3D,axis=1);
print("make_sum_axis_3D_axis_zero:\n",make_sum_axis_3D_axis_One)
make_sum_axis_3D_axis_Two=np.prod(ar_3D,axis=0);
print("make_sum_axis_3D_axis_zero:\n",make_sum_axis_3D_axis_Two)