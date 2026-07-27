def generate_sum(n):
    if n == 1:
        return 1;
    else:
        return n + generate_sum(n-1);

if __name__ == "__main__":    
    get_number = int(input("enter the number:"));
    print(generate_sum(get_number));