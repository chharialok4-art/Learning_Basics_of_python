li001 =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
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
