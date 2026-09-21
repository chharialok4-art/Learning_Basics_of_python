import numpy as np;
def find_max_axis_zero(arr):
    get_max=[];
    for item in arr:
        get_max.append(np.max((item),axis=0))
    print("axis_Zero:\n",get_max);
def find_max_axis_one(arr):
    get_max=[];
    for item in arr:
        get_max.append(np.max((item),axis=1))
    print("Axis One:\n",get_max);
def find_max_axis_two(arr):
    get_max=np.max((arr),axis=2)
    print("Axis Two:\n",get_max);
if __name__=="__main__":
    arr_3D=np.array([[[10,20,90],[12,43,98]],[[65,96,67],[34,56,78]]]).reshape(2,2,3);
    print("Original:\n",arr_3D);
    find_max_axis_zero(arr_3D);
    find_max_axis_one(arr_3D);
    find_max_axis_two(arr_3D);

    