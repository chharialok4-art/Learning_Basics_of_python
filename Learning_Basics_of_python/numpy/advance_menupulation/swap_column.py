import numpy as np;
arr_2D=np.arange(0,9,1).reshape(3,3);
print("Original:\n",arr_2D);
arr_2D[:,[0,2]]=arr_2D[:,[2,0]];
print("Swapped:\n",arr_2D);