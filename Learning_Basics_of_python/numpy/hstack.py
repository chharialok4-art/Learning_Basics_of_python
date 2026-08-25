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
print("-------------------------------hstack 3D to 3D-------------------------------------------")
ar01=np.array([[[1,2,3],[100,200,300]],[[101,202,303],["a","b","c"]],[["AB","CD","EF"],["A01","B02","C03"]]]);
ar02=np.array([[["A1","B2","C3"],["A100","B200","C300"]],[["A101","B202","C303"],["1a","2b","3c"]],[["01AB","02CD","03EF"],["001A01","002B02","003C03"]]]);
make_hstack_3D_to_3D=np.hstack((ar01,ar02));
print("Shape make_vstack_3D_to_3D:",make_hstack_3D_to_3D.shape);
print("make_vstack_3D_to_3D:\n",make_hstack_3D_to_3D);
NOTE="if you give 3D array to hstack it is not match 1 to 1 of ar01 to 1 to 1 of ar02."