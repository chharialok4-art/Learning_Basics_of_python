get_number = int(input("Enter number:-"));
get_factors =[];
for item in range(1,get_number+1,1):
    if get_number % item == 0:
        get_factors.append(item);
    else:
        continue;
print(get_factors);
print("-------------------------------------------------------------------------------")
get_factors001 = [item for item in range(1,get_number+1,1) if get_number%item == 0]
print(get_factors001)
        