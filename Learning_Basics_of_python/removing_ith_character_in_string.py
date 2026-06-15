str001 = "PythonProgrammingLanguage";
get_spread =[]
get_char = str(input("enter the character:"));
for item in str001:
    if item  == get_char:
        continue;
    else:
        get_spread.append(item); 
combine_all = "".join(get_spread);
print(combine_all);
