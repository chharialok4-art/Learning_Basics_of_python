s = 'geeksforgeeks is best';
d = {'e': '1', 'b': '6', 'i': '4'};
get_collectives = [];
for item in s:
    if item not in d.keys():
        get_collectives.append(item);
    else:
        get_collectives.append(d[item]);
print("".join(get_collectives));