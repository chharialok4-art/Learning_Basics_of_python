test_list = [2, 4, 6, 8];
get_factors_frequency=[];
for item in test_list:
    for next_item in range(1,item+1,1):
        if item % next_item == 0:
            get_factors_frequency.append(next_item);
print(get_factors_frequency);
print("-------------------------------------------------------------------------------------------")
def make_dict(get_factors):
    count_dict =[];
    for item in get_factors:
        count_dict.append((item,get_factors.count(item)))
    convert_set_dict = dict(sorted(dict(set(count_dict)).items(), key= lambda x: x[0]));
    return(convert_set_dict);
print(make_dict(get_factors_frequency));

