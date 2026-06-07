if __name__ == "__main__":
    dict001 ={
        "Alok":{"val":100,"time":"31-04-2024"},
        "Darshi":{"val":400,"time":"29-05-2012"},
        "Aman":{"val":900,"time":"19-06-2011"},
        "Anil":{"val":300,"time":"12-01-2010"},
        "Ankur":{"val":800,"time":"13-12-2056"},
        "Amit":{"val":200,"time":"24-08-2023"},
        "Anmol":{"val":600,"time":"30-09-2012"},
        "Anshul":{"val":500,"time":"27-10-2045"},
        "Ashkat":{"val":700,"time":"26-02-2055"},
        "shubham":{"val":600,"time":"25-03-2034"},
        "Rupali":{"val":900,"time":"15-06-2065"},
        "Raunak":{"val":400,"time":"05-09-2014"},
        };
    dict002 = {
        "Anil":{"val":310,"time":"22-04-2015"},      # same val
        "Ankur":{"val":850,"time":"14-08-2021"},
        "Anmol":{"val":690,"time":"05-03-2017"},     # same val
        "Ashkat":{"val":750,"time":"28-09-2016"},
        "shubham":{"val":650,"time":"13-01-2024"},
        "Rupali":{"val":990,"time":"21-10-2022"},    # same val
        "Raunak":{"val":450,"time":"07-05-2013"},
        "Alok":{"val":150,"time":"11-02-2022"},
        "Aman":{"val":950,"time":"09-11-2020"},
        "Amit":{"val":250,"time":"30-12-2019"},
        "Darshi":{"val":490,"time":"18-07-2018"}, 
        "Anshul":{"val":550,"time":"17-06-2023"},
    };
sampliztion = {};
for item,vals in dict001.items():
    for next_item,next_vals in dict002.items():
        if item == next_item:
            if item[0] > next_item[0]:
                sampliztion.update({item:vals});
            else:
                sampliztion.update({item:next_vals});
        else:
            continue;
for item,vals in sampliztion.items():
    print(item,":",vals);