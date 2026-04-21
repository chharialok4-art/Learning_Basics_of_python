from collections import defaultdict;
import multiprocessing as mp;
dictCreate = defaultdict(list);
dictCreate["fruits"].append("apple");
dictCreate["fruits"].append("banana");
dictCreate["fruits"].append("Papaya");
dictCreate["fruits"].append("plam");
dictCreate["Vegies"].append("tomato");
dictCreate["Vegies"].append("LadyFinger");
print(dictCreate);
set001 = ["potato","apple","banana","Papaya","plam","tomato","LadyFinger","apple","banana","Papaya","plam","tomato","LadyFinger"];
createDict001 = defaultdict(list);
for item in set001:
    createDict001[item].append(item);
print(dict(createDict001));
print("------------------------------------------------------------------------------------");
print("No of CPU's in the system:-",mp.cpu_count());

