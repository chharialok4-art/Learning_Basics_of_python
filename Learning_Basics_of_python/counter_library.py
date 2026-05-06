from collections import Counter;
string001 = "qwertyuiopaqwertyuiosdfghjkl";
cnt = Counter(string001);
print(cnt);
getUnique = [{item:vals} for item,vals in cnt.items() if vals>1];
print("getUnique:",getUnique);