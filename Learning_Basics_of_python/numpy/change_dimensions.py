import numpy as np;
print("-----------------------------Broadcast 001 to 002-----------------------------------------");
arr001=np.array([1,2,3]);
arr002=np.array([[100],[200],[300]]);
make_broadcast_001_to_002=np.broadcast(arr001,arr002);
for idx,item in make_broadcast_001_to_002:
    print(idx,":",item);
print("-----------------------------Broadcast 002 to 001-----------------------------------------");
make_broadcast_002_t0_001=np.broadcast(arr002,arr001);
for idx,item in make_broadcast_002_t0_001:
    print(idx,":",item);
print("-----------------------------Expand Dims-----------------------------------------");
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Original Shape:",arr.shape);
print("Original Array:\n",arr);
expend_at_zero=np.expand_dims(arr,axis=0);
print("Expanded Shape At Zero:",expend_at_zero.shape);
print("Expand At Zero:\n",expend_at_zero);
expend_at_one=np.expand_dims(arr,axis=1);
print("Expend shape at One:",expend_at_one.shape);
print("Expend At One:\n",expend_at_one);
expend_at_two=np.expand_dims(arr,axis=2);
print("Expend shape at Two:",expend_at_two.shape);
print("Expend At Two:\n",expend_at_two);
expend_at_three=np.expand_dims(arr,axis=3);
print("Expend shape at three:",expend_at_three.shape);
print("Expend At three:\n",expend_at_three);
print("-------------------------------squeeze-------------------------------------------")
arr_sample=np.array([[[1],[2],[3],[4]]]);
print("Before Squeeze:",arr_sample);
make_squeeze=np.squeeze(arr_sample);
print("After Squeeze:",make_squeeze);
