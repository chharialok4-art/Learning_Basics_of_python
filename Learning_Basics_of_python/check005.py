my_Global_Var = 100;
def my_Func():
    my_Local_Var = 200;
    # global my_Global_Var;
    # my_Global_Var = 300;
    print("Global Variable:",my_Global_Var);
    print("Local Variable:",my_Local_Var);
my_Func();
print("Global Variable:",my_Global_Var);
li001 = [("Alok",100),("Ankur",200),("Amit",300),("Annu",400),("Darshi",500),("Anmol",600)];
for kys,vals in li001:
    print(kys+":",vals);
print("-------------------------------------------------------------------------------------------------")
li002 = [["Alok",100],["Ankur",200],["Amit",300],["Annu",400],["Darshi",500],["Anmol",600]];
for kys,vals in li002:
    print(kys+":",vals);

a,b = (10,20);
print(a,b);

# c,d = {"Alok":100,"Ankur":200,"Amit":300,"Annu":400,"Darshi":500,"Anmol":600};
# print(c);  not possible to unpack dictinary in this way
# c,d = {"Alok":100,"Ankur":200,"Amit":300,"Annu":400,"Darshi":500,"Anmol":600}.items();
# print(c);
# print(d); this will give error because items() will return list of tuples and we are trying to unpack it in 2 variables which is not possible