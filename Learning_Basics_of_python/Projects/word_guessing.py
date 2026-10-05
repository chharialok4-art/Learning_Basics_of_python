import random;
def guessing(generate_randon):
    chance=7
    get_word=[];
    for _ in range(1,len(generate_randon),1):
        get_char=str(input("Choose character now:-"));
        get_word.append(get_char);
        if get_char not in generate_randon:
            chance=chance-1;
            print(f"Try once Again : {chance} left");
            continue;
        for item in generate_randon:
            if item in get_word and chance>0:
                print(item,end="");
            else:
                print("_",end="")
        
if __name__=="__main__":
    group_of_words=["Apple","Banana","cherry","Orange","Guawa","Grapes","Kiwi"];
    generate_randon=random.choice(group_of_words);
    print("List:-",group_of_words);
    print("Random Word:-",generate_randon);
    guessing(generate_randon)