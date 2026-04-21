import json;
with open("/Users/dev/Downloads/airports.json","r") as airPort_files:
    data = json.load(airPort_files);
getAirpots = data["airports"];
getfiltered= [{"Name":nextItem["name"],"City":nextItem["city"],"Country":nextItem["country"]} for nextItem in getAirpots]
getInput = str(input("Enter the Airport name\n"));
searchForInd = list(filter(lambda x:x["Country"] == getInput,getfiltered));

if not searchForInd:
    print("Not Found");
else:
    print(searchForInd);
