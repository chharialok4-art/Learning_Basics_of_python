import math;
arr01 = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41];
get_value = int(input("enter the number:"));
count = int(math.log(len(arr01),2));
starting=0;
ending=len(arr01);
mid=0;
if get_value<arr01[ending-1]:
    for item in range(0,len(arr01),1):
        mid=int((ending+starting)/2);
        if arr01[mid]==get_value:
            print("Found");
            break;
        elif arr01[mid]<get_value:
            starting=mid;
            continue;
        elif arr01[mid]>get_value:
            ending=mid;
            continue;
        else:
            print("Not Found");
else:
    print("Not Found");


