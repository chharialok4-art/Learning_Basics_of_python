liOfTup = [("a", 1), ("b", 2), ("c", 3)];

getConverted002 ={item[0]:item[1] for item in liOfTup};
print(getConverted002);
print("------------------------------------------------------------------------------------------");
dict001={};
for item in liOfTup:
    dict001.update({item[0]:item[1]})
print(dict001);