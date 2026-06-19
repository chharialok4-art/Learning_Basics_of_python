if __name__ == "__main__":
    str001 = "The quick brown fox jumps over the lazy dog";
    judgement =None;
    for item in str001:
        if item != " ":
            if (ord(item) >= 97 and ord(item) <= 122) or (ord(item)>= 65 and ord(item) <= 90):
                judgement = "A Pangram";
            else:
                judgement = "Not a Pangram";
                break;
        else:
            continue;
print(judgement)