li001 = [1,2,3,4,5,6,7,8,2,1];
getInput = int(input("Enter number:"));
havingIndexes = [kys for kys,vals in enumerate(li001) if vals == getInput]
print(havingIndexes[1]-havingIndexes[0]);