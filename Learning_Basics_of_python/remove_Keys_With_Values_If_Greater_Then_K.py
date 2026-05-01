dict001 = {"Alok":100,"Aman":200,"Darshi":300,"Amit":400,"Annu":500,"Pannu":600,"Happy":700,"Ankur":800};
get_input = int(input("Enter number between 100 to 800:-"));
getFiltered = {kys: vals for kys, vals in dict001.items() if vals>get_input};
print(getFiltered);