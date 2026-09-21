import numpy as np 
def ignore_nan_calculate_mean(arr):
    return(np.nanmean(arr))
if __name__=="__main__":
    arr = np.array([[20, 15, 37], [47, 13, np.nan]]);
    print("Original:\n",arr);
    print(ignore_nan_calculate_mean(arr));