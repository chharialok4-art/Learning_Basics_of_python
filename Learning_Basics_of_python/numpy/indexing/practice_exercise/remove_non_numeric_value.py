import numpy as np;
n_arr = np.array([[10.5, 22.5, np.nan], [41, 52.5, np.nan]])
get_nan=~np.isnan(n_arr);
print(get_nan)
print(n_arr[get_nan]);