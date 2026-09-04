import numpy as np;
arr_001=np.array([10,20,600,70,45,55,20,70]);
arr_002=np.array([350,60,10,600,70,20]);
result,idx001,idx002=np.intersect1d(arr_001,arr_002,return_indices=True);
print("result:\n",result);
print("idx001:\n",idx001);
print("idx002:\n",idx002);
