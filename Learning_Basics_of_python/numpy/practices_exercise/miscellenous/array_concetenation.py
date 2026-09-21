import numpy as np;
def concetinate_array(arr001,arr002):
    new_arr=np.concatenate((arr001,arr002),axis=0);
    return new_arr;
if __name__=="__main__":
    arr001=np.array([[100,200],[101,202]]).reshape(2,2,-1);
    print("original Array 001:\n",arr001);
    arr002=np.array([[10,20],[1000,2000]]).reshape(2,2,-1);
    print("original Array 001:\n",arr002);
    print("After conctenate:-\n",concetinate_array(arr001,arr002));