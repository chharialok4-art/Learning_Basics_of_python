li001 = [1,8,3,7,4,5,2,0,6,9,10,56,32,57,90,22];
getNeibour = [];
for item in range(0,len(li001),1):
    if item == 0:
        if li001[item] < li001[item+1]:
            getNeibour.append((li001[item],li001[item+1]));
        else:
            pass;
    elif item > 0 and item != len(li001)-1:
        if li001[item-1] < li001[item+1]:
            getNeibour.append((li001[item],li001[item+1]));
        elif li001[item-1] > li001[item+1]:
            getNeibour.append((li001[item],li001[item-1]));
        else:
            pass;
    else:
        getNeibour.append((li001[item],li001[item-1]));


print(getNeibour);
