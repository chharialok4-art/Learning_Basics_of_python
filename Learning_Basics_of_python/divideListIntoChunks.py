li001 = [1,2,3,4,5,6,7,8,9,10,11];
enterChunks = int(input("enter the chunks:"));
getChunked = [li001[item:item+enterChunks] for item in range(0,len(li001),enterChunks)];
print(getChunked);


