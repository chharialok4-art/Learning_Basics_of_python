test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8];
getCount = [(item,test_list.count(item)) for item in test_list];
convertIntoSet = set(getCount);
print(convertIntoSet);
getKValue = int(input("Enter the K number:\n"));
print("__________________________________________________________________________________________")
for item in convertIntoSet:
    if item[1] == getKValue:
        print(item[0]);
    else:
        pass;

