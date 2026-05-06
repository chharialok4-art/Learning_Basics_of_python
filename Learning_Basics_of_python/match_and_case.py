def month (n):
    match n:
        case "Jan":
            return ("January",31,"Winter");
        case "Feb":
            return ("February",28,"Winter");
        case "Mar":
            return ("March",31,"Winter");
        case "Apr":
            return ("April",30,"Summar");
        case "May":
            return ("May",31,"Summar");
        case "Jun":
            return ("June",30,"Summar");
        case "Jul":
            return ("July",31,"Rainy");
        case "Aug":
            return ("August",30,"Rainy");
        case "Sept":
            return ("September",31,"Rainy");
        case "Oct":
            return ("October",30,"Rainy");
        case "Nov":
            return ("November",31,"Winter");
        case "Dec":
            return ("December",30,"Winter");
        case _:
            return ("No Season","No Days","Nothing Feels Like");
Season = str(input("Enter the Season:"));
Month,Days,FeelsLike = month(Season);
print(f"Month:{Month}\nDays:{Days}\nFeels Like:{FeelsLike}");



