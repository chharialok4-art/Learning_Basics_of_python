dict003 = {
    "Alok": {"Lname":"Chhari","EmployeeId":2200112,"Address":"Indore","Marks":780},
    "Ankur": {"Lname":"Chhari","EmployeeId":2432134,"Address":"Delhi","Marks":721},
    "Amit": {"Lname":"Mansingh","EmployeeId":2209765,"Address":"Gwalior","Marks":743},
    "Anil": {"Lname":"Singh","EmployeeId":22456754,"Address":"Morena","Marks":756},
    "Annu": {"Lname":"Mansingh","EmployeeId":27654312,"Address":"Gwalior","Marks":709},
    "Aman": {"Lname":"Badhoria","EmployeeId":2209764,"Address":"Noida","Marks":767},
    "Darshi": {"Lname":"Badhoria","EmployeeId":220234321,"Address":"Delhi","Marks":745},
    "Happy": {"Lname":"Singh","EmployeeId":2745362,"Address":"Gwalior","Marks":787},
};

print("-------------------------------------map Dict003-----------------------------------------------");

resultMapDict003 = list(map(lambda x : x[1]["EmployeeId"],dict003.items()));
print("resultMapDict003:",resultMapDict003);

print("-------------------------------map getting multiple Entries-------------------------------------");
