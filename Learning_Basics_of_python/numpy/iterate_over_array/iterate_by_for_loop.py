import numpy as np;
print("------------------------------Iterate 1D array------------------------------------------------")
arr_1D=np.arange(0,10,1).flatten();
for item in arr_1D:
    print(item,end=",");
print("\n------------------------------Iterate 2D array------------------------------------------------")
arr_2D=np.arange(0,9,1).reshape(3,3);
for i in range(0,3,1):
    for j in range(0,3,1):
        print(f"[{i},{j}]",arr_2D[i,j]);
print("------------------------------Iterate 2D array direct method------------------------------------------------")
for item in arr_2D:
    print(item);
print("------------------------------changing array value itself------------------------------------------------")
serise_arr=np.arange(0,9,1);
for item in range(0,len(serise_arr),1):
    serise_arr[item]=serise_arr[item]*100;
print(serise_arr);
