str001 = ["Lion", "Li", "Tiger", "Tig", "orange", "ora", "Amsterdam", "Ams"];
get_input = str(input("enter the string:"));
get_resembilance = [item for item in str001 if get_input in item];
print(get_resembilance);