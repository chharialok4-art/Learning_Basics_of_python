def merge(li_odd,li_even):
    combine_all=[];
    ODD=0;
    EVEN=0;
    for _ in range(0,len(li_odd)+len(li_even),1):
        if EVEN>=(len(li_even)):
            combine_all.extend(li_odd[ODD:]);
            return combine_all;
        elif li_even[EVEN] < li_odd[ODD]:
            combine_all.append(li_even[EVEN]);
            print("EVEN:-",EVEN)
            EVEN=EVEN+1;
        else:
            combine_all.append(li_odd[ODD]);
            print("ODD:-",ODD)
            ODD=ODD+1;
if __name__=="__main__":
    li_odd=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51];
    li_even=[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40];
    print(merge(li_odd,li_even));
    
    

