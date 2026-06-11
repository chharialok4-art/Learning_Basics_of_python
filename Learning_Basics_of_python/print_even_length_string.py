str001 = "alok chhari is a bad boy . even thought he held his shirt";
get_splited = str001.split();
put_even_len_string = [];
for item in get_splited:
    if len(item)%2==0:
        put_even_len_string.append(item+",");
    else:
        continue;
join_all = "".join(put_even_len_string);
get_refresh_string = join_all.replace(","," ");
print(get_refresh_string);

