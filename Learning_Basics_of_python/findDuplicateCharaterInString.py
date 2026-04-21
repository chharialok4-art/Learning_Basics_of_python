string001 = "asdfghjklwertyuiopasdfghjklasdfghjklwertyuiozxcvbnm";
getCount=[];
for item in string001:
   getCount.append((item,string001.count(item)));
print("getCount:",getCount);
print("--------------------------------------------------------------------------------------------")
getUnique = set(getCount);
print("getUnique:",getUnique);