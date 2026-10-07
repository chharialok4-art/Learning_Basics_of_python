import random;
if __name__=="__main__":
    list_of_numbers=["110011","123456","101010","221100","112233"];
    generate_random_number=random.choice(list_of_numbers);
    print("enter the user input:-\n");
    temp_arr=[];
    for _ in generate_random_number:
        if "".join(temp_arr)==generate_random_number:
            print("Number fully match.")
            break;
        get_user_input=str(input(""))
        temp_arr.append(get_user_input);
        for item in generate_random_number:
            if item in temp_arr:
                print(item,end="");
                temp_arr.append(item)
            else:
                print("_",end="");
        print("\n");
    if "".join(temp_arr)!=generate_random_number:
        print("number is not match");
    