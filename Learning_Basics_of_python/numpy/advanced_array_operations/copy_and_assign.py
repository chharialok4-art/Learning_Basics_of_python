import numpy as np;
print("-----------------------------Assignment------------------------------------------")
arr_2D=np.arange(0,6).reshape(2,3);
assignment_arr_1D=arr_2D;
assignment_arr_1D[0,1]=1000;
print("Original:\n",arr_2D);
print("Assigned:\n",assignment_arr_1D);
print("-------------------------------------Copy------------------------------------------------")
arr002=np.arange(100,200,10).reshape(2,5);
copied_arr002=arr002.copy();
copied_arr002[0,4]=111111;
print("Original:\n",arr002);
print("Copied Array:\n",copied_arr002);