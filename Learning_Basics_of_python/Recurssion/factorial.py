def fact(get_number):
    if get_number == 1:
        return 1;
    else:
        return get_number * fact(get_number -1);

if __name__ == "__main__":
    get_fact_number = int(input("enter the number:"));
    print(fact(get_fact_number));