import random;
if __name__=="__main__":
    generate_random_number=random.randint(1,10)
    for _ in range(0,7,1):
        guess_number=int(input("enter the number between 1 to 10:-"));
        if generate_random_number==guess_number:
            print("You made it");
            break;
        elif generate_random_number < guess_number:
             print("Too heigh make low");
             continue;
        elif generate_random_number > guess_number:
             print("Too Low make heigh");
             continue;