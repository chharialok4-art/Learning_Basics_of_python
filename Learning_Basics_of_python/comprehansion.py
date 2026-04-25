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
getData006 = [(item,nextItem) for item in li001 for nextItem in fruits]
print("getData006->",getData006);
print("----------------------------------------006------------------------------------------------")
getData007 = [{item:nextItem} for item in li001 if item %2==0 for nextItem in fruits];
print("getData007->",getData007);
print("----------------------------------------007------------------------------------------------")
getData008 = [{nextItem:item} for nextItem in fruits for item in li001 if item %3==0];
print("getData008->",getData008)
print("----------------------------------------008------------------------------------------------")
getData009 = [li001[item:item+3] for item in range(0,10,1)];
print("getData009->",getData009);
print("----------------------------------------009------------------------------------------------")
getData010 = [{nextItem:item} for item in li001 if item % 3==0 for nextItem in li001 if nextItem%2==0];
print("getData010->",getData010);
print("----------------------------------------010------------------------------------------------")
getData011= [{nextItem:item} for item in li001 if item%2==0 for nextItem in fruits];
print("getData011->",getData011);
print("----------------------------------------011------------------------------------------------")



