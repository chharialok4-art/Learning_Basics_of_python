NOTE01="dot and matmul operations are give same result if you take 1D and 2D array";
NOTE02="The difference shows up when you take 1 3D array or Both 3D array";
import numpy as np
arr001=np.array([[[1,2],[3,4]],[[0,1],[1,0]]]);
arr002=np.array([[[5,6],[7,8]],[[1,0],[0,1]]]);
print("arr001:\n",arr001);
print("----------------------")
print("arr002:\n",arr002);
print("-----------------------------------------Dot operation------------------------------------------------")
make_dot=np.dot(arr001,arr002);
print("Make Dot:\n",make_dot);
print("---------------------------------------matmul operation-------------------------------------------")
make_matmul=np.matmul(arr001,arr002);
print("Arr001:\n",arr001);
print("-------------------------");
print("Arr002:\n",arr002);
print("Make matmul:\n",make_matmul);
