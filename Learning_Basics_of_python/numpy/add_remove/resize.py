import numpy as np;
arr_1D=np.arange(0,12,1).reshape(1,12);
print(arr_1D);
print("------------------------------------Resize 1D array(3,4)----------------------------------------")
arr_1D_resize_3_4=np.resize(arr_1D,(3,4));
print("arr_1D_resize:\n",arr_1D_resize_3_4);
print("------------------------------------Resize 1D array(6,2)----------------------------------------")
arr_1D_resize_6_2=np.resize(arr_1D,(6,2));
print("arr_1D_resize:\n",arr_1D_resize_6_2);
print("------------------------------------Resize 2D array()----------------------------------------")
arr_2D=np.arange(0,24,1).reshape(6,4);
print("arr_2D:\n",arr_2D)
print("----------------------------------------------------------------------------------")
arr_2D_resize_2_3_4=np.resize(arr_2D,(2,3,4));
print("arr_2D_resize_2_3_4:\n",arr_2D_resize_2_3_4);