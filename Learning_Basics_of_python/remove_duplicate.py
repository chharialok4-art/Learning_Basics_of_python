d = {'a': [1, 2, 3], 'b': [3, 4, 5], 'c': [5, 6]};
getCollectives = [];
for item in d.values():
    for nextItem in item:
        getCollectives.append(nextItem);
print(set(getCollectives));

print("------------------------------------------------------------------------------------------");
a = {'a': [1, 2, 3], 'b': [3, 4, 5], 'c': [5, 6]};

tempSet = set();
makeDir = {}
for item , vals in a.items():
    addNext =[];
    for nextItem in vals:
        if nextItem not in tempSet:
            addNext.append(nextItem);
            tempSet.add(nextItem);
    makeDir[item] = addNext;

print(makeDir);