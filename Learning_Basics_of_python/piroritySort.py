liOfDict = [{"ID":1001, "Name":"John", "Age":25},
            {"ID":1002, "Name":"Jane", "Age":30},
            {"ID":1034, "Name":"Alok", "Age":22},
            {"ID":1065, "Name":"Ankur", "Age":21},
            {"ID":1078, "Name":"Amnit", "Age":29},
            {"ID":1012, "Name":"Alice", "Age":87},
            {"ID":1087, "Name":"Rupali", "Age":56},
            {"ID":1048, "Name":"Amnol", "Age":87},
            {"ID":1065, "Name":"Disha", "Age":43},
            {"ID":1043, "Name":"Ranurak", "Age":29},
            {"ID":1091, "Name":"Ali", "Age":41},
            {"ID":1020, "Name":"Jind", "Age":19},
            {"ID":1030, "Name":"parul", "Age":27},
            ]
getInout = int(input("Enter the ID\n"));
getData001 = [item for item in liOfDict if item["ID"] == getInout]
print(getData001);
liOfDict.insert(0,getData001[0]);
print(liOfDict);


