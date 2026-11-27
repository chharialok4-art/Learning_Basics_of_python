import pandas as pd
import numpy as np
sris_001=pd.Series(
    [2400,5000,2500,None,1400,3900,4300,None,6700,None,1000],
    index=["Aman","Ankur","Neeraj","Alok","darshi","Chichoo","Nikku","Shyna","Anil","Annu","Vivek"]
)
print("\n\n\n--------------------Count None-----------------------------------------------")
print(sris_001.isna().sum())
print("\n\n\n--------------------Drop None-----------------------------------------------")
sris_001=sris_001.dropna()
print(sris_001)
print("\n\n\n--------------------Replace None with Zero-------------------------------------")
sris_002=pd.Series(
    [24001,50001,25001,None,14001,39001,43001,None,67001,None,10001],
    index=["Aman","Ankur","Neeraj","Alok","darshi","Chichoo","Nikku","Shyna","Anil","Annu","Vivek"]
)
sris_002=sris_002.fillna(0)
print(sris_002)
print("\n\n\n--------------------Replace None with Mean--------------------------------------")

sris_003=pd.Series(
    [240010,500010,250010,None,140010,390010,430010,None,670010,None,100010],
    index=["Aman","Ankur","Neeraj","Alok","darshi","Chichoo","Nikku","Shyna","Anil","Annu","Vivek"]
)
print(sris_003.fillna(sris_003.mean()))
sris_003=sris_003.fillna(sris_003.mean())
print(sris_003[sris_003==340010.0])
print("\n\n\n--------------------finding Unique Values--------------------------------------")
sris_004=pd.Series(
    [1000,4000,4000,2000,7000,5000,7000,4000,9000,1000,2000],
    index=["Aman","Ankur","Neeraj","Alok","darshi","Chichoo","Nikku","Shyna","Anil","Annu","Vivek"]
)
print(sris_004.unique())
print(sris_004.nunique())
print("\n\n\n--------------------Count Values--------------------------------------")
print(sris_004.value_counts().sort_values())
print("\n\n\n--------------------n largest values--------------------------------------")
print(sris_004.nlargest(4))
print("\n\n\n--------------------n smallest values--------------------------------------")
print(sris_004.nsmallest(4))
print("----------------------------replacing None with median---------------------------------------------------")
marks_family = pd.Series(
    [250, 350, None, 450, None, None ,550, 650,550,350],
)
print(marks_family.fillna(marks_family.median()))
print("----------------------------drop None with reset Index---------------------------------------------------")
print(marks_family.dropna().reset_index(drop=True))
print("----------------------------drop None without reset Index---------------------------------------------------")
print(marks_family.dropna())
print("----------------------------Replace---------------------------------------------------")
import pandas as pd
s = pd.Series([10, 20, 30, 20, 40, 20])
result = s.replace(20, 99)
print(result)
print("----------------------------Replace multiple values---------------------------------------------------")
result = s.replace({
    10: 100,
    99: 200,
    30: 300
})
print(result)
print("----------------------------Replace with Zero---------------------------------------------------")
s_001 = pd.Series([10, np.nan, 30,np.nan, 50])
result = s_001.replace(np.nan, 0)
print(result)
print("----------------------------forward Fill---------------------------------------------------")
s_100 = pd.Series([10, np.nan, np.nan, 40, np.nan, 60,70,90,100,np.nan,np.nan])
print(s_100.ffill(limit=3))
print("----------------------------backward Fill---------------------------------------------------")
print(s_100.bfill(limit=4))