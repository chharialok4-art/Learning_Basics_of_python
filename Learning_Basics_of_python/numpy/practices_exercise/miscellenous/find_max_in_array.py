import numpy as np;
def find_max(arr):
    return np.max(arr);
if __name__=="__main__":
    ar_1D=np.arange(0,27,1);
    print("Original:\n",ar_1D);
    print(find_max(ar_1D))