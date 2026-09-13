import numpy as np;
arr_2D=np.arange(0,9,1).reshape(3,3);
print("Original:\n",arr_2D);
arr_2D[:,[0,2]]=arr_2D[:,[2,0]];
print("Swapped:\n",arr_2D);
print("---------------------------------Other Way----------------------------------------")
dtype=[("A",int),("B",int),("C",int)]
arr_2D_002=np.array([(100,120,140),(160,180,200),(220,240,260)],dtype=dtype);
print("Original:\n",arr_2D_002);
arr_2D_002[["A","C"]]=arr_2D_002[["C","A"]];
print("Swaped:\n",arr_2D_002);
