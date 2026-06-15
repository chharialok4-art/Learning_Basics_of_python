import random;
li001 = ["stone","paper","scissor"];
get_viraj = random.choice(li001);
input("Start-->>");
print("Viraj:",get_viraj);
get_alok = random.choice(li001);
input();
print("Alok:",get_alok);
if get_alok == "stone" and get_viraj == "paper":
    print("Paper");
elif get_alok == "stone" and get_viraj == "scissor":
    print("Rock");
elif get_alok == "paper" and get_viraj == "scissor":
    print("scissor");
else:
    print("---------XXXXXXXXXX------------")



