li001 = [1,2,3,4,5,6,7,8,9,10];
# i=0;
# while li001[i]<6:
#     print(li001[i]);
#     i=i+1;

getData = [com_item for item in li001 if (com_item :=item+0.1)>6];
print(getData);

