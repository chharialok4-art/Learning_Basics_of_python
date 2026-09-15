import numpy as np;
arr_3D=np.array([[[10,20,30],[100,200,300]]]);
print("Original Size",arr_3D.shape);
print("Before Squeeze:\n",arr_3D)
print("-----------------------------first Squeeze-----------------------------------");
make_squeeze=np.squeeze(arr_3D);
print("Squeeze Size:\n",make_squeeze.shape)
print("After Squeeze:\n",make_squeeze);
print("-----------------------------Second Squeeze-----------------------------------");
make_further_squeeze=np.squeeze(make_squeeze);
print("Further Squeeze Size:\n",make_further_squeeze);
print("After Squeeze:\n",make_further_squeeze);