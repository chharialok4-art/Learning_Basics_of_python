if __name__=="__main__":
    flames_dict={"f":"friends",
                  "l":"lovers",
                  "a":"affaction",
                  "m":"marriage",
                  "e":"enemies",
                  "s":"siblings"}
    flame_string="flames";
    boy=str(input("Enter the boy name:-"))
    girl=str(input("Enter the girl name:-"))
    for item in boy:
        if item in girl:
            girl=girl.replace(item,"");
            boy=boy.replace(item,"");
    comman_string=list(boy+girl)
    for item in flame_string:
        if item in comman_string:
            get_idx=comman_string.index(item);
            del comman_string[get_idx];
        else:
            continue;
    comman_string_to_str="".join(comman_string)
    for item in comman_string_to_str:
        if item in flame_string:
            print(flames_dict[item],end=",")
        else:
            print("No relation")

