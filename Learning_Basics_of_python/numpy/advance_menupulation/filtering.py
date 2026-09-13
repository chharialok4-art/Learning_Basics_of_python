import numpy as np;
customer_details=np.array([("Alok",20,"Indore"),("Aman",19,"Noida"),
                           ("Darshi",15,"Guna"),("Kirti",12,"Gwalior"),
                           ("Neeraj",34,"Indore"),("Amit",23,"Gwalior"),
                           ("Bulbul",13,"Aron"),("Ankur",34,"Indore"),
                           ("Suraj",45,"Guna")],dtype=[("Name","U10"),("Age",int),("Address","U10")]);
print("Name","| Age","| Address");
print("---------------------------")
for item in customer_details:
    print(item[0],"| ",item[1],"| ",item[2]);
print("------------------------------------------filtering-------------------------------------------------")
print(customer_details[customer_details["Age"]>20])
print("------------------------------------------Accessing-------------------------------------------------")
print(customer_details["Age"]);
