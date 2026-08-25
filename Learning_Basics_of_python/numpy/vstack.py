import numpy as np
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print("-------------------------------vstack 1D to 1D-------------------------------------------")
make_vstack=np.vstack((array1,array2));
print("Shape make_vstack:",make_vstack.shape);
print("make_vstack:",make_vstack);
arr001 = np.array([1, 2, 3])
arr002 = np.array([[4, 5, 6], [7, 8, 9]])
print("-------------------------------vstack 1D to 2D-------------------------------------------")
make_vstack_1D_to_2D=np.vstack((arr001,arr002));
print("Shape make_vstack_1D_to_2D:",make_vstack_1D_to_2D.shape);
print("make_vstack_1D_to_2D:\n",make_vstack_1D_to_2D);
print("-------------------------------vstack 2D to 1D-------------------------------------------")
make_vstack_2D_to_1D=np.vstack((arr002,arr001));
print("Shape make_vstack_2D_to_1D:",make_vstack_2D_to_1D.shape);
print("make_vstack_2D_to_1D:\n",make_vstack_2D_to_1D);
print("-------------------------------vstack 2D to 2D-------------------------------------------")
arr01 = np.array([[4, 5, 6], [7, 8, 9]])
arr02 = np.array([[400, 500, 600], [700, 800, 900]])
make_vstack_2D_to_2D=np.vstack((arr01,arr02));
print("Shape make_vstack_2D_to_2D:",make_vstack_2D_to_2D.shape)
print("make_vstack_2D_to_2D:\n",make_vstack_2D_to_2D);
print("-------------------------------vstack 3D to 3D-------------------------------------------")
arr001=np.array([[[1,2,3],[100,200,300]],[[101,202,303],["a","b","c"]],[["AB","CD","EF"],["A01","B02","C03"]]]);
arr002=np.array([[["A1","B2","C3"],["A100","B200","C300"]],[["A101","B202","C303"],["1a","2b","3c"]],[["01AB","02CD","03EF"],["001A01","002B02","003C03"]]]);
make_vstack_3D_to_3D=np.vstack((arr001,arr002));
print("Shape make_vstack_3D_to_3D:",make_vstack_3D_to_3D.shape);
print("make_vstack_3D_to_3D:\n",make_vstack_3D_to_3D);
NOTE="It is only for 2D array, if you give 3D array it behave differently";
