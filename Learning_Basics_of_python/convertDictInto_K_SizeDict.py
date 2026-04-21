test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3, 'for' : 4, 'geeks' : 5, 'CS' : 6}
getLenOfDict = len(test_dict);

getfactors = [item for item in range(1,getLenOfDict+1,1) if getLenOfDict % item == 0];
print("you can divide dictionary into following ways:",getfactors);
divideIn = int(input("enter the factors:\n"));

getHop = 0;
convertIntoListOfTup = list(test_dict.items());
print(convertIntoListOfTup);
print("-----------------------------------------001--------------------------------------------------")
# tempDict = {};
# for item in range(0,getLenOfDict,1):
#     tempDict.update([convertIntoListOfTup[item]]);
# print(tempDict);
getNewListOfDict= [];

for item in range(0,getLenOfDict,1):
    if getHop != getLenOfDict:
        getDict = {};
        count = 0   
        for nextItem in range(getHop,divideIn,1):
            getDict.update([convertIntoListOfTup[nextItem]]);
            count = count+1;
        getNewListOfDict.append(getDict);
        getHop = getHop+count;
        divideIn = divideIn+count;   
    else:
        break;
print(getNewListOfDict);
 