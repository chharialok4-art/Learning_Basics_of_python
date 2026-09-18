import numpy as np;
print("----------------------------------Without axis mension---------------------------------------")
arr_2D=np.array([[100,90,200],[111,222,333],[101,202,303]]).reshape(3,3);
print("Original:\n",arr_2D);
print(np.amax(arr_2D));
print("----------------------------------With axis mension---------------------------------------")
print("Axis 1:\n",np.amax(arr_2D,0));
print("Axis 2:\n",np.amax(arr_2D,1));
print("----------------------------------With axis mension 3D---------------------------------------")
arr_3D=np.array([[[101,202],[111,333]],[[404,201],[101,110]],[[909,100],[111,200]]]).reshape(3,2,2);
print("Original:\n",arr_3D);
print("Axis:0\n",np.amax(arr_3D,0));
print("Axis:1\n",np.amax(arr_3D,1));
print("Axis:2\n",np.amax(arr_3D,2));
