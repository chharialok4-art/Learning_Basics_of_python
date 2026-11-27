import pandas as pd
employee_data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha", "Karan"],
    "Age": [25, 29, 35, 27, 31],
    "Salary": [30000, 45000, 60000, 40000, 55000],
    "Department": ["IT", "HR", "IT", "Finance", "HR"]
}
emply_dataframe=pd.DataFrame(employee_data)
print("-------------------------------Greater smaller---------------------------------------------------")
print(emply_dataframe[emply_dataframe["Age"]>=29])
print("-------------------------------Max---------------------------------------------------")
print(emply_dataframe["Salary"].max())
print("-------------------------------Index Operation---------------------------------------------------")
print(emply_dataframe[emply_dataframe["Department"]=="IT"])
print("-------------------------------Mean Median---------------------------------------------------")
print("Median:-",emply_dataframe["Salary"].median(),"Mean:-",emply_dataframe["Salary"].mean())
print("-------------------------------head---------------------------------------------------")
print(emply_dataframe.head())
print("-------------------------------tail---------------------------------------------------")
print(emply_dataframe.tail())
print("-------------------------------Find columns---------------------------------------------------")
print(emply_dataframe.columns.to_list())
print("-------------------------------Find total Index------------------------------------------")
print(emply_dataframe.index)
print("-------------------------------Find total dimension------------------------------------------")
print(emply_dataframe.ndim)
print("-------------------------------specific data------------------------------------------")
print(emply_dataframe.loc[0:2,["Name","Salary"]])
print("-------------------------------Print Row and Column------------------------------------------")
print(emply_dataframe.iloc[2:4,0:3])
print("-------------------------------Accessing Single cell------------------------------------------")
print(emply_dataframe.at[1,"Salary"])
print(emply_dataframe.iat[1,2])
print("-------------------------------Sort value by Column------------------------------------------")
print(emply_dataframe.sort_values(by="Salary",ascending=True))
print("-------------------------------Test------------------------------------------")
print(emply_dataframe.loc[1:3, ["Name", "Salary"]])