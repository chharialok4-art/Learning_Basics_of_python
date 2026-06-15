str001 = "Geeks for Geeks Alok Chhari Singh"
str002 = "Learning from Geeks for Geeks Chhari Rupali"
saturated_str001 = str001.split(" ");
saturated_str002 = str002.split(" ");
result_comman = [];
for item in saturated_str002:
    if item in saturated_str001:
        continue;
    else:
        result_comman.append(item+",");
for item in saturated_str001:
    if item in saturated_str002:
        continue;
    else:
        result_comman.append(item+",");
append_all = "".join(result_comman);
print(append_all.replace(","," "));


        
