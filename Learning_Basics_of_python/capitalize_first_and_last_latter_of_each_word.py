str001 = "My name is alok chhari and i am a crual boy";
get_split = str001.split();
converted_first_and_last =[];
for item in get_split:
    temp_list  = item.split();
    sub_temp = [];
    get_len = len(temp_list);
    first_letter = temp_list[0].upper();
    sub_temp.append(first_letter);
    sub_temp.append(temp_list[1:get_len-1]);
    last_letter = temp_list[get_len-1].upper();
    sub_temp.append(last_letter);
    collect_all = "".join(temp_list);
    converted_first_and_last.append(collect_all);
print(converted_first_and_last);
