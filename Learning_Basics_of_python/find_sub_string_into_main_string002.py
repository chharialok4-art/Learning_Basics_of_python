from collections import Counter;
s1 = 'fnd';
s2 = 'fBoOkBIHnfndBthesibuishlider';
getCollectionsValueS1 = Counter(s1);
getCollectionsValueS2 = Counter(s2);
makeTrue = False;
for item in getCollectionsValueS2:
    if getCollectionsValueS1[item] <= getCollectionsValueS2[item]:
        makeTrue = True;
        continue;
    else:
        makeTrue=False;
        break;
if makeTrue:
    print("Possible");
else:
    print("Not Possible");




