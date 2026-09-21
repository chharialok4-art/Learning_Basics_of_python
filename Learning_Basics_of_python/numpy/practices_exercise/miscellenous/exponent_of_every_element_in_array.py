import numpy as np;
def expo_elements(arr):
    for item in arr:
        print(item**3);
    return 0;
if __name__=="__main__":
    arr_3D=np.arange(100,370,10).reshape(3,3,3);
    print("Original:\n",arr_3D);
    expo_elements(arr_3D);