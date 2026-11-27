import pandas as pd
employee_data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha"],
    "Age": [25, 29, 35, 27],
    "Salary": [30000, 45000, 60000, 40000]
}
print("----------------------------DataFrame-------------------------------------------")

employee_data_frame=pd.DataFrame(employee_data)
print(employee_data_frame)
print("----------------------------DataFrame Max-------------------------------------------")
avg_salary=employee_data_frame.max()
print(avg_salary)
print("-------------------------Serise----------------------------------------------")
custom_salary=pd.Series(
    [1000,2000,5000,9000],
    index=["Alok","Ankur","Aman","Darshi"]
)
print("-------------------------Serise Operations----------------------------------------------")
print(custom_salary)
print(custom_salary.loc["Darshi"])
print(custom_salary.iloc[2])
print(custom_salary.loc[["Alok","Darshi"]])
print(custom_salary.iloc[[0,2]])
print("------------------------------------multi Series Operations--------------------------------------------------------")
sris_001=pd.Series(
    [10,40,32,21,45],
    index=["a","b","c","d","e"]
)
sris_002=pd.Series(
    [900,800,500,300,200],
    index=["e","a","c","b","d"]
)
print(sris_001+sris_002)