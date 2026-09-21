import numpy as np;
def make_sorted_kth(Arr):
    get_indx_sorted=np.argsort(Arr);
    print(Arr[get_indx_sorted][:4])
if __name__=="__main__":
    arr = np.array([23, 12, 1, 3, 4, 5, 6]);
    print("Original:\n",arr);
    make_sorted_kth(arr);