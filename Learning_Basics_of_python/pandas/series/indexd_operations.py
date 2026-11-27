import pandas as pd
sris_001=pd.Series(
    [1000,2000,3000,8000,3000,6000,1000,4500],
    index=["Alok","Ankur","Aman","Amit","Darshi","Annu","Neeraj","Anil"]
)
print(sris_001)
print("-----------------------------Index operations(loc)-----------------------------------------")
print(sris_001.loc["Darshi"])
print("-----------------------------Index operations(iloc)----------------------------------------")
print(sris_001.iloc[6])
print("-------------------Index operations(filtering one condition)---------------------------------")
print(sris_001[sris_001>5000])
print("--------------------Index operations(filtering two condition)---------------------------------")
result= sris_001[(sris_001> 2000) & (sris_001<5000)]
print(result)
print("-----------------------------Index operations(isin)------------------------------------------")
result001=sris_001.isin([1000,8000,4500])
print(sris_001[result001])
