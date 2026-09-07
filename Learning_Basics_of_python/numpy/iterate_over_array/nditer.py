import numpy as np;
print("------------------------------nditer 3D array------------------------------------------------")
arr0010=np.arange(0,27,1).reshape(3,3,3);
for item in np.nditer(arr0010):
    print(item,end=",");
