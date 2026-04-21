a = [["a", 1,"ALOK"], ["b", 2,"ANKUR"], ["c", 3,"AMIT"]];
getDict = [(item,vals,kys) for item,vals,kys in a]
print(getDict);
print("------------------------------------------------------------------------------------------");
b = (("a", 1,"ALOK"), ("b", 2,"ANKUR"), ("c", 3,"AMIT"));
getDict001 = [(item,vals,kys) for item,vals,kys in a]
print(getDict001);