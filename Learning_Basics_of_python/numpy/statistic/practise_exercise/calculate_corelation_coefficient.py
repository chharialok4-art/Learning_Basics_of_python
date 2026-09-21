import numpy as np;
def cal_co_re(ar_1D,ar_1D_001):
    get_correlation=np.corrcoef(ar_1D,ar_1D_001);
    print(get_correlation);
if __name__=="__main__":
    ar_1D=np.arange(100,370,10).flatten();
    ar_1D_001=np.arange(0,27,1).flatten();
    print("Original:\n",ar_1D);
    cal_co_re(ar_1D,ar_1D_001)