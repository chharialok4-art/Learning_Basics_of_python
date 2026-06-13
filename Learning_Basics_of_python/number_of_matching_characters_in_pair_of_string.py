str001 ="sdfghjk";
str002 = "zxcvbnmasdfghjkqwertyuio";
count = 0;
for item in str001:
    if item in str002:
        count = count+1;
    else:
        continue;
print(count);