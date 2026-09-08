import numpy as np;
arr_len_20=np.arange(0,20,1).flatten();
print("-------------------------------------Array slicing-----------------------------------------------")
print("Array:\n",arr_len_20);
print("Slicing:\n",arr_len_20[-2:]);
print("-----------------------Array slicing with Steps-------------------------------------")
print("Slicing with Steps:\n",arr_len_20[::2]);
print("----------------------2D Array slicing with Steps-----------------------------------")
arr_2D=np.arange(0,9,1).reshape(3,3);
print("Array_2D:\n",arr_2D)
print("1st Row All Columns:\n",arr_2D[1,:]);#1st row all columns-[3,4,5]
print("All Rows 1st Column:\n",arr_2D[:,1]);#All Rows 1st Column-[1,4,7]
print("0th row all columns:\n",arr_2D[0,:])#0th row all columns-[0,1,2]
print("all rows 0th column:\n",arr_2D[:,0])#all rows 0th column-[0,3,6]
print("1st row with 0th column:\n",arr_2D[1:,0])#1st row with 0th column[3,6]
print("0th row with 2nd column",arr_2D[0:,2])#0th row with 2nd column[2,5,8]
arr = np.arange(12)
arr_3d = arr.reshape(3, 4)
print("-------------:\n",arr_3d)
print("output:\n",arr_3d[1, 2:4])