if __name__ == "__main__":
    temp_dict = [];
    test_dict = {"a" : {"b" : {"c" : {}}}, "d" : {"e" : {}},"o" : {}, "f" : {"g" : {"h" : {}}}};
    length_of_dict = 0;
    for kys,item in test_dict.items():
        sample_dict = {};
        sample_dict = {kys:sample_dict};
        for sub_kys , sub_item in item.items():
            sample_dict = {sub_kys:sample_dict};
            for sub_sub_kys, sub_sub_item in sub_item.items():
                sample_dict = {sub_sub_kys:sample_dict};
        temp_dict.append(sample_dict);
        del sample_dict;
print(temp_dict);