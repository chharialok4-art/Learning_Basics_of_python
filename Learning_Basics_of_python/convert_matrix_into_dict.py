from collections import defaultdict;
li = [[5, 6, 7], [8, 3, 2], [8, 2, 1]];

dict001 = defaultdict(list);
for keys,item in enumerate(li):
    dict001[keys+1].append(item);
print(dict001);
print("_________________________________________001___________________________________________________");
result001 = {kys+1:vals for kys,vals in enumerate(li)}
print(result001);

print("_________________________________________002___________________________________________________");

li002 = [(5, 6, 7), (8, 3, 2), (8, 2, 1)];
dict002 = defaultdict(list);
for kys,vals in enumerate(li002):
    dict002[kys+1].append(vals)
print(dict002);
print("_________________________________________003___________________________________________________");
dict003={};
for kys ,vals in enumerate(li):
    dict003[kys+1] = vals;
print(dict003);
print("_________________________________________004___________________________________________________");
li001 = [1,2,3,4,5,6,7,8,9,10];
dict006 = defaultdict(list);
for kys,vals in enumerate(li001):
    dict006[kys+1].append(vals+100)
print(dict006);