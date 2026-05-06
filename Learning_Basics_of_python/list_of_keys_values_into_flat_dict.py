li001 = [("name", "Ak"), ("age", 25), ("city", "NYC")];
getDict = {item[0]:item[1] for item in li001};
print(getDict);
print("-----------------------------");
getDict002 = {item:nextVals for item,nextVals in li001}
print(getDict002);