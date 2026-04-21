a = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}];
getCollectives =[];
for item in a:
    getCollectives.append(item.values());
print(getCollectives);
print("-------------------------------------------------------------------------------------");
getvalues=[];
for item in a:
    getvalues.append([itemValues for itemValues in item.values()]);
print(getvalues);
