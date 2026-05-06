test_dict = {"a" : {"b" : {"c" : {}}}, "d" : {"e" : {}},"o" : {}, "f" : {"g" : {"h" : {}}}};
print("-------------------------------Follow this one time------------------------------------------")
kysList = [];
finalList =[];
for idx,vals in test_dict.items():
    if idx not in kysList:
       kysList.append(idx);
    else:
        continue;
    for sub_kys , sub_vals in vals.items():
        if sub_kys not in kysList:
            kysList.append(sub_kys);
        else:
            continue;
        for sub_sub_kys , sub_sub_vals in sub_vals.items():
            if sub_sub_kys not in kysList:
                kysList.append(sub_sub_kys);
            else:
                continue;
            finalList.append(list(kysList));
print(finalList);
