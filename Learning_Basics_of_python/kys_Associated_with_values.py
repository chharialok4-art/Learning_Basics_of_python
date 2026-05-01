from collections import defaultdict;
d = {'gfg': [1, 2, 3], 'is': [1, 4], 'best': [4, 2]};
get_set_of_values = defaultdict(list);
for kys,vals in d.items():
   for item in vals:
      get_set_of_values[item].append(kys);
print(get_set_of_values);