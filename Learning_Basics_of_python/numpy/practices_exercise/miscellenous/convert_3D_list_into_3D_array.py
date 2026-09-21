import numpy as np;
def convert_into_array(arr):
    arr_3D=np.array(arr);
    print("Concerted:\n",arr_3D);
if __name__=="__main__":
    data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]];
    print("original:\n",data);
    convert_into_array(data);
    