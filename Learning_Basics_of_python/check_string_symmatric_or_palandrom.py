import math;
str001 = str(input("Enter String:\n"));
get_length = len(str001);
divide_str = math.ceil(len(str001)/2);
if get_length%2==0:
    if str001[0:divide_str] == str001[divide_str:get_length]:
        print(str001,":is palindrom");
    else:
        print("Not a palindrom");
else:
    if str001[0:divide_str-1] == str001[divide_str:get_length]:
        print(str001,":is palindrom");
    else:
        print("Not a palindrom");