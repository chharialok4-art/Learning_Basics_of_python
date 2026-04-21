dict001 =  {"Fname":"Alok","Lname":"Chhari","EmployeeId":2200112,"Address":"Indore","Marks":780};
dict001Percentage = {**dict001,"Percentage":(dict001["Marks"]/800)*100};
print(dict001Percentage)

list001 = [
    {"Name":"Alok"},
    {"Name":"Alok"},
    {"Name":"Alok"},
    {"Name":"Alok"},
           ];
AddRollNo = [{**vlue,"rollNum":indx}for indx, vlue in enumerate(list001)]
print("Add_Roll_Number:",AddRollNo);

list002 = [1,2,3,4,5,6,7,8,9,10];
ModifyList002 = list(map(lambda x:x+2,list002));
print("Modify List:",ModifyList002);