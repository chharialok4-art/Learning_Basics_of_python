import pandas as pd
import numpy as np
s1 = pd.Series([100, 200, 300], index=["A", "B", "C"])
s2 = pd.Series([10, 20, 30], index=["B", "C", "D"])
result = s1.sub(s2)
print("substraction:-\n",result)
result001=s1.sub(s2,fill_value=0)
print("Addition:-\n",result001)
print("---------------------------------Combine All---------------------------------------------")
s_001=pd.Series(
    [10,20,40,60,80,np.nan,100,np.nan,200,np.nan],
    index=["A","S","D","F","G","H","J","K","L","P"]
)
s_002=pd.Series(
    [10,20,40,60,80,9999,100,8888,200,7777],
    index=["A","S","D","F","G","H","J","K","L","P"]
)
print(s_001.combine_first(s_002))
print("---------------------------------Update---------------------------------------------")
print(s_001.update(s_002))
