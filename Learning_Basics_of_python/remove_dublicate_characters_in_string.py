str001 = "asdfghjklasdfghjklqasdfghjklqwertyuiowertyuioqwertyuiozxcvbnmzxcvbnm";
print("Original:",str001)
count_dict = {};
combine_all = [];
for item in str001:
    if item not in count_dict:
        temp_count = str001.count(item);
        count_dict.update({item:temp_count});
    else:
        continue;
for item in count_dict:
    combine_all.append(item);
get_collected = "".join(combine_all);
print("filtered:",get_collected);


