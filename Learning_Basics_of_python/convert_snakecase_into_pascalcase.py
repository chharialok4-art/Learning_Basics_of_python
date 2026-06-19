str001 = "sadfghjk_wertyu_zxcvbnm_234567_asdfghkjhgfd";
expand_all = [];
for item in range(0,len(str001),1):
    if str001[item] != "_":
        expand_all.append(str001[item]);
    else:
        expand_all.append(str001[item+1].upper());
        item = item+1;
print("".join(expand_all));
