inititilizer = 0;
test_dict = {"Gfg" : 4, "is" : 4, "Best" : 4, "for" : 4, "Geeks" : 4};
print(len(test_dict));
LocalInititilizer = inititilizer;
for item in test_dict.values():
    LocalInititilizer = item +LocalInititilizer;
findMean = LocalInititilizer/len(test_dict);
print(findMean);
