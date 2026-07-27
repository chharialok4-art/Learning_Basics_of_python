def palindrome(num_limit):
    if num_limit < 1:
        return;
    else:
        print(num_limit,end=" ");
        palindrome(num_limit-1);
        print(num_limit,end=" ");
        return;

if __name__ == "__main__":
    get_numbers_limit = int(input("enter the number:"));
    print(palindrome(get_numbers_limit));