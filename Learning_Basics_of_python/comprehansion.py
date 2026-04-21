li001 = [1,2,3,4,5,6,7,8,9,10];
fruits = ['apple','banana','grapes','orange','kiwi'];
getData001 = [item*2 for item in li001 if item==7];
print("getdata001->",getData001);
print("----------------------------------------001------------------------------------------------")
getData002 = [item*2 if item==7 else item for item in li001];
print("getData002->",getData002);
print("----------------------------------------002------------------------------------------------")
getData003 = [item for item in li001 if item > 6 and item <9];
print("getData003->",getData003);
print("----------------------------------------003------------------------------------------------")
getData004 = [(item,nextItem) for item in li001 if item >4 and item <8 for nextItem in fruits];
print("getData004->",getData004);
print("----------------------------------------004------------------------------------------------")
getData005 = [(item,nextItem) for item in fruits for nextItem in li001 if nextItem >= 8];
print("getData005->",getData005);
print("----------------------------------------005------------------------------------------------")
