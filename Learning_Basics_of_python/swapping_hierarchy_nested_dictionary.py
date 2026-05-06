test_dict = {'Gfg': { 'a' : [1, 3, 7, 8], 'b' : [4, 9], 'c' : [0, 7]}} ;
print("---------------------------------Worst Way----------------------------------------------------")
finalDict = {};
for kys,vals in test_dict['Gfg'].items():
    tempDict = {};
    tempDict.update({"Gfg":vals});
    finalDict.update({kys:tempDict});
print(finalDict);
print("---------------------------------Best Way----------------------------------------------------")
new_Dict = {};
for mainKey,subDict in test_dict.items():
    for next_keys, next_vals in subDict.items():
        tempDict = {};
        tempDict.update({mainKey:next_vals});
        new_Dict.update({next_keys:tempDict});
print(new_Dict);





