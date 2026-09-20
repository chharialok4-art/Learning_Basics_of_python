import numpy as np;
ar_3D=np.arange(0,27,1).reshape(3,3,3);
print("Original:\n",ar_3D);
varience_3D_axis_zero=np.var(ar_3D,axis=0)
print("varience_3D_axis_zero\n",varience_3D_axis_zero);
varience_3D_axis_one=np.var(ar_3D,axis=1)
print("varience_3D_axis_one\n",varience_3D_axis_one);
varience_3D_axis_two=np.var(ar_3D,axis=2)
print("varience_3D_axis_two\n",varience_3D_axis_two);