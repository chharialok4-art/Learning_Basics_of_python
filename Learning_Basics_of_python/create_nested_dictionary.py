a = {'Gfg': 4, 'is': 5, 'best': 9, "Good": 23}
b = [8, 3, 2, 4];
getZiped ={};
for idx,(kys,vals) in enumerate(a.items()):
    getCollects ={};
    getCollects.update({kys:vals})
    getZiped.update({b[idx]:getCollects})
print(getZiped);
    # print(f"{idx}:({kys},{vals})");
    # createDict={};
print("--------------------------------------001------------------------------------------")
for item in ("Alok",100):
    print(item);
print("--------------------------------------002------------------------------------------")
xyz = ("Alok",200);
print(dict([xyz]));
print("--------------------------------------003------------------------------------------")
marwels =list(a.keys());
for item in marwels:
    if item == "Good":
        print("item:",item)
    else:
        print(item);
