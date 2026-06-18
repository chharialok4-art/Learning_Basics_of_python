str001 = "ksgee";
str002 = "geeks";
elongate = list(str001);
count = 0;
for item in range(0,len(str001),1):
    if "".join(elongate) == str002:
        break;
    else:
        item_pop = elongate.pop();
        elongate.insert(0,item_pop);
        count = count+1;
print(count);
