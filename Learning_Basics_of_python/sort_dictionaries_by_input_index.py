test_list = [{"Gfg" : [6, 7, 8], "is" : 9, "best" : 10}, 
             {"Gfg" : [2, 0, 3], "is" : 11, "best" : 19},
             {"Gfg" : [4, 6, 9], "is" : 16, "best" : 1}];
initialization_key = str(input("enter the key:-"));
get_Dict = sorted(test_list , key = lambda x : x[initialization_key], reverse = False );
print(get_Dict);
    
