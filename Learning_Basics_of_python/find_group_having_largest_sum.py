li001 =[[1, 10], [2, 11], [3, 12], [4, 13], [5], [6], [7], [8], [9]];
getSum =[];
get_max =[[0]];
for item in li001:
    if len(item) != 2:
        getSum.append(item);
    else:
        sum = item[0]+item[1];
        item.insert(0,sum);
        getSum.append(item);
for item in getSum:
    if item[0] > get_max[0][0]:
        get_max.pop();
        get_max.append(item);
    else:
        continue;
get_max[0].pop(0);
print(get_max[0]);
