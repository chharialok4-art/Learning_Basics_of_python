str001= 'geeksforgeeks is best for geeks';
get_input  = str(input("enter the input string:"));
get_splited = str001.split(" ");
for item in range(0,len(get_splited),1):
    if get_splited[item] == get_input:
        print("desire String ->",item);
    else:
        continue;