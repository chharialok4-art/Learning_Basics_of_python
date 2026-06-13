str001 ="qwertyquioasdfghjklzxcvbnm";
count_dict ={};
collect_all = [];
for item in str001:
    if item not in count_dict:
        temp_count = str001.count(item);
        count_dict.update({item:temp_count});
    else:
        continue;
get_min = min(count_dict.values());
for item,next in count_dict.items():
    if next == get_min:
        collect_all.append(item);
print("".join(collect_all));
