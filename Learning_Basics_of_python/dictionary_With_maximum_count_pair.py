test_list = [{"gfg": 2, "best" : 4}, {"gfg": 2, "is" : 3, "best" : 4, "CS" : 9}, {"gfg": 2}];
get_length_of_Dictionary =[];
for item in test_list:
    get_length_of_Dictionary.append(len(item));
print(max(get_length_of_Dictionary));
getDict = [item for item in test_list if len(item) == max(get_length_of_Dictionary)];
print(getDict);