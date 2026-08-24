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

