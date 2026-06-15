if __name__ == "__main__":
    str001 = "01010101010101111110000101010100001010101010101000010101111010101010";
    count = 0;
    for item in str001:
        if item == "0" or item == "1":
            count = count +1;
        else:
            break;
    if count == len(str001):
        print("String is Binary");
    else:
        print("not a binary");
