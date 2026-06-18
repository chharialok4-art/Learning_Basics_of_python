str001 = "aaasssdddsssaaaqqqwwweeeffffffffccccccvvvvaaaaassss";
rem = str001[0];
print(rem,end="");
for item in str001:
    if rem == item:
       continue;
    else:
       rem = item;
       print(rem,end="")
