import os;
test_dict = {'Nikhil' : {'English' : 5, 'Maths' :  2, 'Science' : 14},
             'Akash' : {'English' : 15, 'Maths' :  7, 'Science' : 2},
             'Akshat' : {'English' : 5, 'Maths' :  50, 'Science' : 20}};
new_dict = {kys:dict(sorted(vals.items(),key = lambda x:x[1])) for kys,vals in test_dict.items()};
print(new_dict);
print("---------------------------------------------------------------------------------------------")
for sn,(key, value) in enumerate(os.environ.items()):
    print(f"{sn}:- {key} : {value}");
# print(os.environ);