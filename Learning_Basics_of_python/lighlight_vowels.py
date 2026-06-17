str001 ="qwertyuiopasdfghjkl;zxcvbnmasdfghjqwertyuiozxcvbnm,asdfghjklwertyuiop";
vowels = ["a","e","i","o","u"];
for item in str001:
    if item in vowels:
        print(item.upper(),end="");
    else:
        print(item,end="");
