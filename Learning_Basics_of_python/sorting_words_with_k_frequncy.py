if __name__ == "__main__":
    li001 = ["geekforgeekss", "is", "bessst", "for", "geeks"];
    li001 = sorted([{item:item.count("s")} for item in li001], key = lambda x:list(x.values())[0],reverse=True);
    print(li001);