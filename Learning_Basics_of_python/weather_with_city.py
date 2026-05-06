import json;
with open("Users/dev/Downloads/weather.json","r") as weather_file:
    getData = json.load(weather_file);
# print(getData["weather"]);
# print("_____________________________________________________________________________________");
getSpecficWeather = {};
getCities=[];
for item in getData["weather"]:
    getCities.append(item["cityName"]);
print(getCities);
getCity = str(input("Enter the city Name:\n"));
for item in getData["weather"]:
    if item["cityName"] == getCity:
        getSpecficWeather.update(item);
    else:
        pass;
print(f"City_Name:{getSpecficWeather["cityName"]}\nWeather:{getSpecficWeather["currentConditions"]}\nTemperature:{getSpecficWeather["temperature"]}/C\nWind_Speed:{getSpecficWeather["windSpeed"]}n/m\nWind_Direction:{getSpecficWeather["windDirection"]}");
