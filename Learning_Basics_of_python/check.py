li001 =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25];
incre = 1;
count = 0;
another = 1;
tempList =[];
for item in range(0,len(li001),1):
    if another <= len(li001):
        tempList.append(li001[count:another])
        count = another; 
        incre = incre+1;
        another = incre+count; 
    else:
        break;
print(tempList);
    