import numpy as np
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
make_dstack=np.dstack((array1,array2));
print("-----------------------------------dstack 1D to 1D--------------------------------------------")
print("Shape make_dstack:",make_dstack.shape);
print("make dstack:\n",make_dstack);
print("-----------------------------------dstack 2D to 2D--------------------------------------------")
array1 = np.array([[10, 20, 30], [40, 50, 60]])
array2 = np.array([[70, 80, 90], [100, 110, 120]])
make_dstack_2D_to_2D=np.dstack((array1,array2));
print("Shape make_dstack_2D_to_2D:",make_dstack_2D_to_2D.shape);
print("make_dstack_2D_to_2D:\n",make_dstack_2D_to_2D);
print("-----------------------------------dstack 3D to 3D--------------------------------------------")
arr001=np.array([[[1,2,3],[100,200,300]],[[101,202,303],["a","b","c"]],[["AB","CD","EF"],["A01","B02","C03"]]]);
arr002=np.array([[["A1","B2","C3"],["A100","B200","C300"]],[["A101","B202","C303"],["1a","2b","3c"]],[["01AB","02CD","03EF"],["001A01","002B02","003C03"]]]);
make_dstack_3D_to_3D=np.dstack((arr001,arr002));
print("Shape make_dstack_2D_to_2D:",make_dstack_3D_to_3D.shape);
print("make_dstack_2D_to_2D:\n",make_dstack_3D_to_3D);