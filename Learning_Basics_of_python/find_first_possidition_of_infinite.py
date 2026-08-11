li001 = [9,8,7,6,2,3,4,5,6,7,5,17,8,9,9,76,"@","@","@","@","@","@","@","@","@","@","@","@","@","@","@","@","@","@","@","@","@","@","@","@"];
def get_posidition(arr):
    starting=0;
    ending=len(arr)-1;
    for item in range(0,len(arr),1):
        mid=int((starting+ending)/2);
        print("MID:-",mid,"starting:-",starting,"ending:-",ending);
        if isinstance(arr[mid],int) and isinstance(arr[mid+1],int):
            starting=(mid+1);
            continue;
        if arr[mid]=='@'and arr[mid-1]=="@":
            ending=(mid-1);
            continue;
        if isinstance(arr[mid],int) and arr[mid+1]=="@":
            return (mid+1);
        if isinstance(arr[mid-1],int) and arr[mid]=="@":
            return (mid);
pos = get_posidition(li001);
print(pos);
    

