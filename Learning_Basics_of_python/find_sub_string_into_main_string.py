from collections import Counter;
s1 = 'ALOKCHHARI';
s2 = 'fBoOkBIHnfndBthesibuishlider';
getCountS1 = Counter(s1);
print(getCountS1);
getCountS2 = Counter(s2);
print(getCountS2);
getCollectivesS1=[]
getCollectivesS2 =[]
for item , vals in getCountS1.items():
    getCollectivesS1.append((item,vals));
getLengthForS1 = len(getCollectivesS1);
for item ,vals in getCountS2.items():
    getCollectivesS2.append((item,vals));
getLengthForS2 = len(getCollectivesS2);
print(getCollectivesS1);
print(getCollectivesS2);
noOfTrues =[];
for item in getCollectivesS1:
    for nextItem in getCollectivesS2:
        if item[0] != nextItem[0]:
            continue;
        else:
            if item[1] != nextItem[1]:
                noOfTrues.append(False);
            else:
                noOfTrues.append(True);
                break;
if len(noOfTrues) != len(getCollectivesS1):
    print("Not Achieve");
elif False not in noOfTrues:
    print("Achieved");
else:
    print("Not Achieved");

    




