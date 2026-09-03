import numpy as np;
def make_sort_with_lex(arr_names,arr_marks):
    lexico=np.lexsort((arr_names,arr_marks));
    combine_all=[];
    for item in range(0,len(lexico),1):
        combine_all.append((arr_names[lexico][item],arr_marks[lexico][item]))
        # print(arr_names[lexico][item],":",arr_marks[lexico][item])
    for item in combine_all:
        print(item[0],":",item[1]);
if __name__=="__main__":
    arr_names=np.array(["Alok","Darshi","Aman","Ankur","Amit","Neeraj","Anil","Luis","Annu","Kirti","Priti"])
    arr_marks=np.array([900,300,200,800,700,1100,200,500,100,340,290]);
    make_sort_with_lex(arr_names,arr_marks);