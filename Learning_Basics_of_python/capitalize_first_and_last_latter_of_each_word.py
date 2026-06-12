str001 = "My name is alok chhari and i am a crual boy";
get_split = str001.split();
final_sting = [];
temp_string = [];
first = 0;
last = 0;
for item in get_split:
    get_len = len(item);
    if get_len == 1:
        first = item[0].upper()
        final_sting.append(first);
    else:
        first = item[0].upper()
        temp_string.append(first);
        temp_string.extend(item[1:len(item)-1].lower());
        last = item[len(item)-1].upper();
        temp_string.append(last);
        get_final = "".join(temp_string);
        final_sting.append(get_final);
        temp_string.clear();
print(" ".join(final_sting));