import pandas as pd
employee_data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha", "Karan"],
    "Age": [25, 29, 35, 27, 31],
    "Salary": [30000, 45000, 60000, 40000, 55000],
    "Department": ["IT", "HR", "IT", "Finance", "HR"]
}
employee_dataframe=pd.DataFrame(employee_data)
print(employee_dataframe)
print("--------------------------------Select One column-------------------------------------------------")
print(employee_dataframe[["Name","Department"]])
print("--------------------------------Select specific column by index-------------------------------------------------")
print(employee_dataframe.iloc[2])
print("--------------------------------Select specific column by value-------------------------------------------------")
print(employee_dataframe.loc[2,"Department"])