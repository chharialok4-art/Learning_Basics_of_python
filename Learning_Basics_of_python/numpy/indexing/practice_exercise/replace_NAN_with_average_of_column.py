import numpy as np;
arr = np.array([[1.3, 2.5, 3.6, np.nan], [2.6, 3.3, np.nan, 5.5], [2.1, 3.2, 5.4, 6.5]])
print("Original:\n",arr);
find_nan=np.isnan(arr);
print("get NAN:\n",find_nan);
find_position_of_nan=np.where(find_nan)
print("Position:\n",find_position_of_nan);
get_mean=np.nanmean(arr,axis=0);
print("Mean of array:\n",get_mean);
arr[find_position_of_nan]=np.take(get_mean,find_position_of_nan[1]);
print("Complete array:\n",arr);
