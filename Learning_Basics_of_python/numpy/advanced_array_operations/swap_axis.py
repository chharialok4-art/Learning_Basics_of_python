import numpy as np;
arr_3X2=np.arange(0,6,1).reshape(3,2);
print("--------------------------------Axis Swap 3X2 to 2X3---------------------------------------------")
print("Original:\n",arr_3X2);
arr_2X3=np.swapaxes(arr_3X2,0,1);
print("arr_2X3:\n",arr_2X3);
print("----------------------------------Axis Swap 3X2 to 2X3---------------------------------------------------")
print(np.swapaxes(arr_3X2,1,0));



