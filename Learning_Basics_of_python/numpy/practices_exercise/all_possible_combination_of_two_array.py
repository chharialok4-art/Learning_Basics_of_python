import numpy as np;
a = np.array([1, 2])
b = np.array([4, 6])
get_X=np.array(np.meshgrid(a,b)).T.reshape(-1,2);
print(get_X);
