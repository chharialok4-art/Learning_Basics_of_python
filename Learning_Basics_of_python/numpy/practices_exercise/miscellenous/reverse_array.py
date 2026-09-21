import numpy as np;
def reverse_array(arr001):
    return np.flip((arr001),axis=1);
if __name__=="__main__":
    arr001=np.arange(0,9,1).reshape(3,3);
    print("Original:\n",arr001);
    print("Reversed:\n",reverse_array(arr001));
