import numpy as np
def calculate_mean(Input):
    get_mean_collectives=[];
    for item in Input:
        get_mean_collectives.append(np.mean(item))
    return get_mean_collectives;
if __name__=="__main__":
    Input = [np.array([1, 2, 3]),
             np.array([4, 5, 6]),
             np.array([7, 8, 9])];
    print("original:\n",Input);
    get_mean=calculate_mean(Input);
    for idx,item in enumerate(get_mean):
        print(idx,":-",item);
