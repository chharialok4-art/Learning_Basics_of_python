import pandas as pd
data = [
    {"Name": "Aman", "Age": 24},
    {"Name": "Neeraj", "Salary": 45000},
    {"Name": "Alok", "Age": 25, "Salary": 40000}
]
df = pd.DataFrame(data)
print(df)