import numpy as np;
def get_indx(arr):
    make_indx=np.argsort(arr);
    print("Indexes:-\n",make_indx);
if __name__=="__main__":
    arr=np.array([30, 10, 20,90,43,21,92,31,63]);
    get_indx(arr);
