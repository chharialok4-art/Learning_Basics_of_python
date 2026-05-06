test_list = [1, 3, 4, 6, 5, 1, 1, 0];
getCount = [(item,test_list.count(item)) for item in test_list];
convertIntoSetThenList = list(set(getCount));
print(convertIntoSetThenList);
getValuesWithoutOccurence = [];
for item in convertIntoSetThenList:
    if item[1] == 1:
        getValuesWithoutOccurence.append(item[0]);
    else:
        pass;
print(getValuesWithoutOccurence);