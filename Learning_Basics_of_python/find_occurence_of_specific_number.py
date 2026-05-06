from collections import defaultdict;
test_list = [(4, 5, 6, 4, 4), (4, 4, 3), (4, 4, 4), (3, 4, 9)];
getNumber = int(input("Enter the Number:-"));
getOccurence = int(input("Enter the Number of Ocurence:-"));
getNumberOfOccurence = defaultdict(list);
for item in test_list:
    getCount ={};
    for nextItem in item:
        getCount.update({nextItem:item.count(nextItem)})
        getNumberOfOccurence.update({item:getCount});
print(getNumberOfOccurence);
print("_________________________________________________________________________________________________________")
gettuple =[];
for kys,vals in getNumberOfOccurence.items():
    if getNumber in kys:
        if vals[getNumber] == getOccurence:
            gettuple.append(kys);
        else:
            pass;
    else:
        pass;
print(gettuple);


