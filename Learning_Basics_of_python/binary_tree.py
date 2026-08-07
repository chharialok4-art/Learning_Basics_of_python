import math;
searching_value = int(input("enter the number:"));
arr001 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];
starting = 0;
ending = len(arr001);
mid = 0;
while arr001[mid] != searching_value:
    mid = int((ending+starting)/2);
    if arr001[mid] > searching_value:
        ending = mid;
    else:
        starting = mid;

