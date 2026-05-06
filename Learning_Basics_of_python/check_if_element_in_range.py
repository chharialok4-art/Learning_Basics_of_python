a = [20, 50, 40, 30, 10];

low = 20;
high = 50;

a.sort(reverse=False);
print(a);
getLengthOfList = len(a);
if a[0]<=low and a[getLengthOfList-1]<=high:
    print("In range");
else:
    print("Not In range");


