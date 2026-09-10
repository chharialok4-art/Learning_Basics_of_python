import numpy as np;
arr_3X2=np.arange(0,6,1).reshape(3,2);
print("--------------------------------Axis Swap 3X2 to 2X3---------------------------------------------")
print("Original:\n",arr_3X2);
arr_2X3=np.swapaxes(arr_3X2,0,1);
print("arr_2X3:\n",arr_2X3);
print("----------------------------------Axis Swap 3X2 to 2X3---------------------------------------------------")
print(np.swapaxes(arr_3X2,1,0));
print("----------------------------------Axis Swap 3X2 to 2X3---------------------------------------------------")
arr_1X4=np.arange(0,4,1).flatten();
print("Original arr_1X4:\n",arr_1X4);
arr_4X1=np.swapaxes(arr_1X4,1,0);
print("Result arr_4X1:\n",arr_4X1)
print("----------------------------------DO for 3D array---------------------------------------------------")


