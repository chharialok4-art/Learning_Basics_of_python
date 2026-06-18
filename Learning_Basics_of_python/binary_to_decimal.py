num = "10";
sum_all =0;
temp =0;
for item in range(0,len(num),1):
    temp = int(num[item]) * 2**((len(num)-1)-item);
    sum_all = sum_all +temp;
print(sum_all);
    


