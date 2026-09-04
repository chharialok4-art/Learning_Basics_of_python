import numpy as np;
arr_001=np.array([10,20,600,70,45,55,20,70]);
arr_002=np.array([350,60,10,600,70,20]);
result=np.isin(arr_001,arr_002);
print(result);
print(arr_001[result]);
