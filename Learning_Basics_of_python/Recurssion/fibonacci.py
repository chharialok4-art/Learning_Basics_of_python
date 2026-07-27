def fibo(terms):
    if terms == 0:
        return 0;
    elif terms == 1 or terms == 2:
        return 1;
    else:
        return fibo(terms-1) + fibo(terms-2);
if __name__ == "__main__":
    number_of_terms = int(input("enter the number of terms:"));
    for item in range(0,number_of_terms,1):
        print(fibo(item),end=",");