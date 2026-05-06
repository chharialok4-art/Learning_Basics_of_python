a = ["name", "age", "city"]  
b = [["Alice", 25, "New York"], ["Bob", 30, "Los Angeles"], ["Charlie", 22,]];
getCollectives = [dict(zip(a,item)) for item in b];
print(getCollectives);

