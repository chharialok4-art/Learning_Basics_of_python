import numpy as np;
arr001=np.array([[3,4,9],[9,8,5],[1,0,3]])
arr002=np.array([10,20,40])
make_solve=np.linalg.solve(arr001,arr002);
for idx,item in enumerate(make_solve):
    print(idx,":",item);