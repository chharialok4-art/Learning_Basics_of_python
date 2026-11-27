import pandas as pd
sris_001=pd.Series(
    [1000,2000,3000,8000,3000,6000,1000,4500],
    index=["Alok","Ankur","Aman","Amit","Darshi","Annu","Neeraj","Anil"]
)
print("\n\n\n-----------------------sort by values----------------------------------------------")
print(sris_001.sort_values())
print("\n\n\n-----------------------sort by index----------------------------------------------")
print(sris_001.sort_index(ascending=False))