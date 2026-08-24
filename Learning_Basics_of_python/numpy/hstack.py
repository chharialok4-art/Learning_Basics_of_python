import numpy as np;
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
make_hstack_array1_and_array2=np.hstack((array1,array2));
print("Shape:",make_hstack_array1_and_array2.shape);
print("make_hstack_array1_and_array2:\n",make_hstack_array1_and_array2);
print("----------------------------------hStack 2D to 1D-----------------------------------------------")
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([7, 8])
convert_arr2=arr2.reshape(-1,1)
print("Shape arr1:",arr1.shape);
print("Shape:",convert_arr2.shape)
print("convert Arr2:\n",convert_arr2);
make_hstack_arr1_and_arr2=np.hstack((arr1,convert_arr2));
print("Shape make_hstack_arr1_and_arr2:",make_hstack_arr1_and_arr2.shape);
print("make_hstack_arr1_and_arr2:\n",make_hstack_arr1_and_arr2);
print("-----------------------------------hstack 2D to 2D-------------------------------------------")
arr001 = np.array([[1, 2], [3, 4]])
arr002 = np.array([[5, 6], [7, 8]])
print("Shape arr001:",arr001.shape);
print("Shape arr002:",arr002.shape);
make_hstack=np.hstack((arr001,arr002));
print("hstack 2D to 2D:\n",make_hstack);