import numpy as np;
def make_sort_with_lex(arr_names,arr_marks):
    lexico=np.lexsort((arr_names,arr_marks));
    joining_arr=[];
    for item in range(0,len(lexico),1):
        print(arr_names[lexico][item],":",arr_marks[lexico][item])
if __name__=="__main__":
    arr_names=np.array(["Alok","Darshi","Aman","Ankur","Amit","Neeraj","Anil","Luis","Annu","Kirti","Priti"])
    arr_marks=np.array([900,300,200,800,700,1100,200,500,100,340,290]);
    make_sort_with_lex(arr_names,arr_marks);