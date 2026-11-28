import pandas as pd
marks = pd.Series(
    [95, 82, 45, 67, 30],
    index=["Aman", "Rahul", "Neeraj", "Vivek", "Anil"]
)
def grade(x):
    if x>=90:
        return "Remarkable"
    elif x>=75 and x<90:
            return "Exellent"
    if x>=65 and x<75:
            return "Very Good"
    if x>=55 and x<65:
            return "Good"
    if x<55:
            return "Fail"
result=marks.map(grade)
print(result)
print("--------------------------------------Other operations in map------------------------------------------")
grades = pd.Series(
    ["A", "B", "C"],
    index=["Excellent", "Good", "Average"]
)
students = pd.Series(
    ["Excellent", "Good", "Excellent", "Average"]
)
print(students.map(grades))
print("---------------------------------Using map for others---------------------------------------------------")
numbers = pd.Series([10, 20, 30, 40])
result = numbers.map(lambda x: x * 2)
print(result)
print("---------------------------------map to upper case strings---------------------------------------------------")
s_001 = pd.Series(["python", "numpy", "pandas"])
result = s_001.map(str.upper)
print(result)
print("-----------------------------------two series mapping-----------------------------------------------")
grade_mapping = {
    1: "Excellent",
    2: "Good",
    3: "Average"
}
result = grades.map(grade_mapping)
grades = pd.Series([1, 1, 3, 4, 3, 2, 1])
print(grades.map(grade_mapping))