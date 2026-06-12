import math;
str001 = "wertyuiasdfghjk";
get_length = len(str001);
get_half_len = math.ceil(get_length/2);
count =0;
get_str =[];
for item in str001:
    if count < get_half_len:
        temp = item.upper();
        get_str.append(temp);
        count= count+1;
    else:
        temp= item.lower();
        get_str.append(temp);
        count= count+1;
make_it_join = "".join(get_str);
print(make_it_join);