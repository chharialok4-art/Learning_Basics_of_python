import numpy as np;
arr_2D=np.arange(0,21,1).reshape(7,3);
print(arr_2D);
check_for=[9,10,11];
print(check_for,":",check_for in arr_2D.tolist());

