a = ["Gfg", "is", "Good", "for", "Geeks"]
d = {"Gfg": 5, "Best": 6, "for":10};
getListOfKeys = [vals for kys,vals in d.items() if kys in a];
print(getListOfKeys);