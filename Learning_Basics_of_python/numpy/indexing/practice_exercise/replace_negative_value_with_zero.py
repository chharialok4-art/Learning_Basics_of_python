import numpy as np;
a = np.array([1, 2, -3, 4, -5, -6]);
a[a<0]=0;
print(a);
print("Customize:\n",a>0)