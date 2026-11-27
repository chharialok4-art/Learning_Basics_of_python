import pandas as pd
a = pd.Series(
    [10, 20, 30],
    index=["A", "B", "C"]
)
b = pd.Series(
    [1, 2, 3],
    index=["B", "C", "D"]
)
print(a + b)