import numpy as np;
def cal_sum(arr):
    make_sum=np.sum(arr);
    return make_sum;
if __name__=="__main__":
    ar_2D=np.arange(10,37,1);
    print("ARRAY:-\n",ar_2D);
    print("SUM :- ",cal_sum(ar_2D));