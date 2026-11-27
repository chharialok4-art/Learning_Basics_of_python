import pandas as pd
sris_004=pd.Series(
    [1000,4000,4000,2000,7000,5000,7000,4000,9000,1000,2000],
    index=["Aman","Ankur","Neeraj","Alok","darshi","Chichoo","Nikku","Shyna","Anil","Annu","Vivek"]
)
print("----------------------------------slicing by Column Label--------------------------------------------------")
print(sris_004.loc["Neeraj":"Nikku"])
print("----------------------------------slicing by Column indexs--------------------------------------------------")
print(sris_004[0:4])
print("----------------------------------slicing by Column indexs--------------------------------------------------")
salary = pd.Series(
    [25000, 35000, 45000, 55000, 65000],
    index=["Aman", "Rahul", "Neeraj", "Vivek", "Anil"]
)
print("-------------------------------Greater And Samller-----------------------------------------------")
print(salary[(salary>=40000) & (salary<=65000)])
print("-------------------------------Between-----------------------------------------------")
print(salary[salary.between(29000,60000,inclusive="both")])
print("-------------------------------Where-----------------------------------------------")
print(salary.where(salary>45000,other="Babblu"))
print("-------------------------------Drop-----------------------------------------------")
new_salary=salary.drop(["Vivek"])  #drop() does not modify the original Series by default.
print(new_salary)
salary_family = pd.Series(
    [25000, 35000, None, 45000, None, None ,55000, 65000],
    index=["Rinki", "Alok", "Neeraj", "Ankur", "Bijendra","Pranjal","Anmol","Aashish"]
)
print("--------------------------------None Position make frist or last-----------------------------")
print(salary_family.sort_values(ascending=True,na_position="first"))
print("--------------------------------unique---------------------------------------------------")
print(salary_family.unique())
print("--------------------------------Number of unique---------------------------------------------------")
print(salary_family.nunique(dropna=False))
marks_family = pd.Series(
    [250, 350, None, 450, None, None ,550, 650,550,350],
    index=["Rinki", "Alok", "Neeraj", "Ankur", "Bijendra","Pranjal","Anmol","Aashish","Ramesh","Suresh"]
)
print("----------------------------------proportion------------------------------------------")
print(marks_family.value_counts(normalize=True)) #<----------------------Important
