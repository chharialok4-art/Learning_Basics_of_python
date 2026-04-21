import json;
with open("Users/dev/Downloads/simple_english_dictionary.json","r") as dictionary:
    getData = json.load(dictionary);
searhFor = str(input("enter keyword:\n"));
print("------>",getData[searhFor]);