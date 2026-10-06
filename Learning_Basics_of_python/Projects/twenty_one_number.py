import numpy as np;
import random;
def bagram(arr):
    initilazaire=1;
    for _ in range(0,len(arr)+1,1):
        if initilazaire>21:
            break;
        computer_generated_random=random.randrange(initilazaire,initilazaire+3);
        print("Computer:-",end=" ")
        for item in range(initilazaire,computer_generated_random+1,1):
            print(item,end=",")
            if item==21:
                print("Computer Loss");
                break;
        initilazaire=computer_generated_random;
        human_generated_random=random.randrange(computer_generated_random,initilazaire+3);
        print("\nEnter the your input")
        for item in range(initilazaire,human_generated_random,1):
            get_human_input=int(input())
            initilazaire=get_human_input;
        initilazaire=initilazaire+1;
        if get_human_input==21:
            print("You loss");
            break;
if __name__=="__main__":
    arr=np.arange(1,22,1).flatten().tolist();
    bagram(arr);