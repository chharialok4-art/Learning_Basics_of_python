from itertools import filterfalse;
print("---------------------------------------Map Dict001---------------------------------------------------------")

dict001_itsNotADictionary_ItIsASet = {1,2,3,4,5,6,7,8,9,10};
resultMapDict001 = list(map(lambda x : x+100 , dict001_itsNotADictionary_ItIsASet));
print("resultMapDict001:",resultMapDict001);

print("---------------------------------------filter Dict001---------------------------------------------------------")

resultFilterDict001 = list(filter(lambda x: x<7 , dict001_itsNotADictionary_ItIsASet));
print("resultFilterDict001:",resultFilterDict001);

print("---------------------------------------filterfalse Dict001---------------------------------------------------------")
resultFilterFalseDict001 = list(filterfalse(lambda x: x<7 , dict001_itsNotADictionary_ItIsASet));
print("resultFilterFalseDict001:",resultFilterFalseDict001);

print("-------------------------------------Comprehansion Dict001-----------------------------------");
resultComprehansionDict001 = [item for item in dict001_itsNotADictionary_ItIsASet if item < 5];
print("resultComprehansionDict001:",resultComprehansionDict001);

print("---------------------------------------for loop Dict001---------------------------------------");
resultForLoopDict001 =[];
for item in dict001_itsNotADictionary_ItIsASet:
    if item < 5:
        resultForLoopDict001.append(item)
print("resultForLoopDict001:",resultForLoopDict001)

print("=====================================================================================================")

dict002 = [
    {"Fname":"Alok","Lname":"Chhari","EmployeeId":2200112,"Address":"Indore","Marks":780},
    {"Fname":"Ankur","Lname":"Chhari","EmployeeId":2432134,"Address":"Delhi","Marks":721},
    {"Fname":"Amit","Lname":"Mansingh","EmployeeId":2209765,"Address":"Gwalior","Marks":743},
    {"Fname":"Anil","Lname":"Singh","EmployeeId":22456754,"Address":"Morena","Marks":756},
    {"Fname":"Annu","Lname":"Mansingh","EmployeeId":27654312,"Address":"Gwalior","Marks":709},
    {"Fname":"Aman","Lname":"Badhoria","EmployeeId":2209764,"Address":"Noida","Marks":767},
    {"Fname":"Darshi","Lname":"Badhoria","EmployeeId":220234321,"Address":"Delhi","Marks":745},
    {"Fname":"Happy","Lname":"Singh","EmployeeId":2745362,"Address":"Gwalior","Marks":787},
]
print("-------------------------------MAP Dict002----------------------------------------------------");
resultMapDict002 = list(map(lambda x : (x["Marks"]/800)*100 , dict002));
print("resultMapDict002:",resultMapDict002);

print("--------------------------MAP Dict002(Sort out Employee With Name and MArks)----------------)");
resultMapDict002Percentage = list(map(lambda x: {**x,"Percentage":x["Marks"]/8},dict002))
print("resultMapDict002Percentage:",resultMapDict002Percentage)

print("----------------------------MAP Dict002 Name and Percentage-----------------------------------");

resultMapDict002NamePercentage = list(map(lambda x: {"name":x["Fname"],"sir_name":x["Lname"],"percent":x["Percentage"]},resultMapDict002Percentage));
print("resultMapDict002NamePercentage:",resultMapDict002NamePercentage)
print("============================Get Three Element================================================");
for item in resultMapDict002NamePercentage:
    print(f"{item["name"]} {item["sir_name"]} : {item["percent"]}%",);

print("------------------------FILTER Dict002---------------------------------------------------------");
resultFilterDict002 = list(filter(lambda x:x["Percentage"]>95,resultMapDict002Percentage));
print("resultFilterDict002:",resultFilterDict002);

print("------------------------FILTERFALSE Dict002---------------------------------------------------------");
resfilterFalseDict002 = list(filterfalse(lambda x: x["Marks"]>740,resultMapDict002Percentage));
print("resfilterFalseDict002:",resfilterFalseDict002);

print("-----------(E-001)------------get entries by comprehansion Dict002---------------------------------------------------------");
resultWithSelected = [{"fname":item["Fname"],"lname":item["Lname"],"NetMarks":item["Percentage"]}for item in resultMapDict002Percentage if item["Percentage"]>95];
print("resultWithSelected:",resultWithSelected);

print("---------------------------filter with map select multiple elements------------------------------");
resultMapWithFilterDict002 = list(map(lambda x: {"f_NAME":x["Fname"],"l_NAME":x["Lname"],"TotalMarks":x["Percentage"]},filter(lambda x: x["Percentage"]>95,resultMapDict002Percentage)))
print("resultMapWithFilterDict002:",resultMapWithFilterDict002);

print("-----------------------------comprehansion dict002------------------------------------------");

resultComprehansionDict002 = [{"f_name":item["Fname"],"l_name":item["Lname"],"Marks":item["Marks"],"percent":(item["Marks"]/8)} for item in dict002 if item["Marks"]>750];
print("resultComprehansionDict002:",resultComprehansionDict002);

print("-----------------------------for loop dict002------------------------------------------");
namePercentDict002 = [];
for item in dict002:
    namePercentDict002.append({"Name":item["Fname"],"SirName":item["Lname"],"percent":item["Marks"]/8});
print("namePercentDict002:",namePercentDict002);

print("======================================================================================================");

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
resultMapMultipleValuesDict003 = list(map(lambda x: {"F_name":x[0],"L_name":x[1]["Lname"],"percent":x[1]["Marks"]/8},dict003.items()))
print("resultMapMultipleValuesDict003:",resultMapMultipleValuesDict003);

print("--------------------------Filter multiple values Dict003----------------------------------");
resultFilterMultipleValuesDict003 = list(map(lambda x: {**x[1],"percent":x[1]["Marks"]/8,"Fname":x[0]},dict003.items()));
print("resultFilterMultipleValuesDict003:",resultFilterMultipleValuesDict003);

selectNameAndPercentDict003 = list(filter(lambda x:x["percent"]<95,resultFilterMultipleValuesDict003))
print("-----------------------------------------fetch Result-------------------------------------------");
print("selectNameAndPercentDict003:",selectNameAndPercentDict003);

print("------------------------------------------Filter False Dict003-------------------------------------------------")
resultFilterFalseDict003 = list(filterfalse(lambda x:x["percent"]<95,resultMapMultipleValuesDict003))
print("resultFilterFalseDict003:",resultFilterFalseDict003);

print("-----------------------------------Map With Filter Dict003--------------------------------------------------")
resultMapWithFilterDict003 = list(map(lambda x:{"F_NAME":x["Fname"],"L_NAME":x["Lname"],"E_ID":x["EmployeeId"],"PERCENT":x["percent"]},filter(lambda x:x["percent"]<95,resultFilterMultipleValuesDict003)))
print("resultMapWithFilterDict003:",resultMapWithFilterDict003);

print("---------------------------------comprehansion Dict003----------------------------------------------------------")
resultComprehansionDict003 = [{item+" "+val["Lname"]: val["Marks"]/8,}for item, val in dict003.items() if (val["Marks"]/8)<97];
print("resultComprehansionDict003:",resultComprehansionDict003);

print("----------------------------------------For loop Dict003--------------------------------------------------")
resultForDict003 =[];
for item , vals in dict003.items():
    resultForDict003.append({vals["Marks"],item});
print("resultForDict003:",resultForDict003);