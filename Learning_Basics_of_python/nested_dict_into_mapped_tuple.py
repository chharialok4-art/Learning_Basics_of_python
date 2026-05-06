from collections import defaultdict;
d = {'gfg': {'x': 5, 'y': 6}, 'is': {'x': 1, 'y': 4}, 'best': {'x': 8, 'y': 3}};
makeDict= [];
makeDict  = defaultdict(tuple);
for item in d.values():
    for nextItem in item:
        makeDict[nextItem] = makeDict[nextItem] + (item[nextItem],);
        # makeDict[nextItem].append(item[nextItem])
print(makeDict);