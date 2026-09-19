import numpy as np;
ar_2D=np.arange(0,27,1).reshape(3,3,3);
print("----------------------------------ar_2D median--------------------------------------")
print("Original:\n",ar_2D);
make_median_2D=np.median(ar_2D,axis=0);
print("make_median_2D_axis_Zero:\n",make_median_2D);
make_median_2D_axis_one=np.median(ar_2D,axis=0);
print("make_median_2D_axis_Zero:\n",make_median_2D_axis_one);
make_median_2D_axis_two=np.median(ar_2D,axis=0);
print("make_median_2D_axis_Zero:\n",make_median_2D_axis_two);
