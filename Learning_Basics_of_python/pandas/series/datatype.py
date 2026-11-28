import pandas as pd
import numpy as np
s = pd.Series(["10", "20", "hello", "40"])
s.index=["A","B","C","D"]
result = pd.to_numeric(s, errors="coerce")
print(result)