dict001 = {"Gfg": [5, 7, 5, 4, 5], "is": [6, 7, 4, 3, 3], "Best": [9, 9, 6, 5, 5]};
getDistinctCount = [(kys,len(set(item))) for kys,item in dict001.items()];
print("getDistinctCount:",getDistinctCount);
getMax = [(None,0)];
for item in getDistinctCount:
    if item[1]>getMax[0][1]:
        getMax.pop();
        getMax.append(item);
print("getMax:",getMax);


