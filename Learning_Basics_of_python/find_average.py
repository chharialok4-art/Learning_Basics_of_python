x=[[1,2,3],[2,1,3,4],[5,6,7,6,5],[8,9,0,4],[0,1,0,2]];
lengthOfx = len(x);
for item in x:
    temp=0
    lenghtOfItem = len(item);
    for subList in item:
        temp= temp+subList;
    item.insert(0,temp/lenghtOfItem);
print(x);
i=0;j=0;
temp=0;
while i<lengthOfx:
    while j<lengthOfx:
        if x[j][0]<x[i][0]:
            temp = x[j];
print("x[1]:",x[1]);
print("x[1][0]:",x[1][0])