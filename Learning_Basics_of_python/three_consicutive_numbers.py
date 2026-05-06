a = [1, 2, 2, 2, 3, 4, 5, 5, 5, 7 ,9,100,200,400,400,400];
counter = 2;
getSequence = [];
for item in range(0,len(a)-2,1):
    if a[item] == a[item+1] and a[item+1] == a[item+2]:
        getSequence.append(a[item]);
        counter = counter+1;
    else:
        counter = counter+1;
        pass;
if not getSequence:
    print("No Sequence Found");
else:
    print(getSequence);
