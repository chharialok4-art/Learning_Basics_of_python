import numpy as np;
def calculate_varience(arr):
    return [np.var(arr),np.std(arr)];
if __name__=="__main__":
    ar_1D=np.arange(0,17,1).flatten();
    print("Original:\n",ar_1D);
    print(calculate_varience(ar_1D));