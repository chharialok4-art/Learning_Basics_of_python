import numpy as np;
def calculate_median(ar_1D):
    return(np.median(ar_1D));
if __name__=="__main__":
    ar_1D=np.arange(0,10,1);
    print("Original:\n",ar_1D);
    get_median=calculate_median(ar_1D);
    print("Median:",get_median);