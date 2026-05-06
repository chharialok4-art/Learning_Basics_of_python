test_dict = {'Alok' : {'Manjeet' : 5, 'Himani' : 10},
             'Manjeet' : {'Manjeet' : 8, 'Himani' : 9},
             'Ankur' : {'Manjeet' : 10, 'Himani' : 15}};
getCollectives=[]
for ky,vals in test_dict.items():
    getSum  = 0;
    for valsInside in vals.values():    
        getSum = getSum+valsInside;
    getCollectives.append((ky,getSum))
print(getCollectives);
getMax = (None,0);
for item in getCollectives:
    if item[1]>getMax[1]:
        getMax = item;
    else:
        continue;
print(getMax);


