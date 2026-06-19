str001 = "alokalokalopkalokalokalokalokalokankurankurankuramitamitamitannuannudarshidarshi";
get_singles =[];
for item in str001:
    if item not in get_singles:
        get_singles.append(item);
    else:
        continue;
print(get_singles);