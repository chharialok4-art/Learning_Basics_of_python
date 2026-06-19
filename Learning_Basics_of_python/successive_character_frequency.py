if __name__ == "__main__":
    str001 = "aloksdfghjkalokzxc vbnmalok234 567alokalokcv bn";
    get_Alok_count = str001.count("alok");
    print(get_Alok_count);
    get_successor = [str001[item+4] for item in range(0,len(str001)-4,1) if str001[item:item+4] == "alok"]
    print(get_successor);
    get_successor = [{item:get_successor.count(item)} for item in get_successor];
    print(get_successor);
