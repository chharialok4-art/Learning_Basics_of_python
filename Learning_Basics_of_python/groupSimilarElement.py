a = ['apple', 'banana', 'apple', 'orange', 'banana'];
collectives =[];
for item in a:
    getCount = a.count(item);
    if(collectives.count(item)):
        continue;
    else:
        for puttingCount in range(0,getCount,1):
            collectives.append(item);
print(collectives);
print("---------------------------Another Methord----------------------------");
getSort = sorted(a, reverse=False);
print(getSort);

    

