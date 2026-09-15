import numpy as np;
def search_elements(arr_2D,search_sequence):
    count=0;
    make_search_sequence=search_sequence.tolist();
    fill_with_elements=[]
    for item in np.nditer(arr_2D):
        fill_with_elements.append(item);
    for item in range(0,len(fill_with_elements)-1,1):
        if make_search_sequence==fill_with_elements[item:item+2]:
            count=count+1
    return count;
if __name__=="__main__":
    arr_2D=np.array([[2, 8, 9, 4],
                    [9, 4, 9, 4],
                    [4, 5, 9, 7],
                    [2, 9, 4, 3]])
    search_sequence=np.array([9, 4]);
    print(search_elements(arr_2D,search_sequence));