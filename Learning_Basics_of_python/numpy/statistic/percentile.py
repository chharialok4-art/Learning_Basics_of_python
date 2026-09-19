import numpy as np;
print("-----------------------------------2D percentile without axis--------------------------------------------")
ar_2D=np.arange(100,190,10).reshape(3,3);
print("Original:\n",ar_2D);
get_percentage=np.percentile(ar_2D,90);
print("Percentile:-",get_percentage)
print("-----------------------------------2D percentile with axis 0--------------------------------------------")
get_percentage_axis_0=np.percentile(ar_2D,90,axis=0);
print("Percentile:-",get_percentage_axis_0)
print("-----------------------------------2D percentile with axis 1--------------------------------------------")
get_percentage_axis_0=np.percentile(ar_2D,90,axis=1);
print("Percentile:-",get_percentage_axis_0)