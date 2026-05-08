dict001 ={'c': [3], 'b': [12, 10], 'a': [19, 4]} ;
newDict ={};
for kys,vals in dict001.items():
        vals.sort(reverse=False)
        newDict.update({kys:vals});
print(newDict);