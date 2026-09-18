import numpy as np;
arr_2D=np.arange(0,6,1).reshape(2,3);
print("Original Array:\n",arr_2D);
print("-------------------------------------Move Array--------------------------------------------")
move_axis=np.moveaxis(arr_2D,0,1);
print("After Move:\n",move_axis);
print("-------------------------------------Swap Axis--------------------------------------------")
swap_axis=np.swapaxes(arr_2D,axis1=0,axis2=1);
print("After Swap:\n",swap_axis)