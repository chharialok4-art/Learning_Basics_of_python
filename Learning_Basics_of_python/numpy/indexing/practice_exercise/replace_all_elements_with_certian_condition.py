import numpy as np;
ar_1D=np.arange(0,9,1).reshape(3,3);
print("Original:\n",ar_1D);
ar_1D[ar_1D>5]=100;
print(ar_1D);