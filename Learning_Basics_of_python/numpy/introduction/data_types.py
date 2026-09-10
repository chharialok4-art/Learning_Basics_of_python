import numpy as np;
dt=np.dtype([("Name","U10"),("Age",np.int16),("Address","U10"),("Roll_number",np.int16)]);
real_data=np.array([("Alok",33,"Indore",400),
                    ("Amit",29,"Gwalior",500),
                    ("Darshi",25,"Delhi",200),
                    ("Anil",39,"Gungaon",309),
                    ("Neeraj",45,"Indore",709)],dtype=dt);
print(dt);
print("-----------------------------------------------------------------------------");
print(real_data);
print("------------------------------Once-----------------------------------------------");
get_ones=np.ones((4*3),order="C")
print(get_ones);
print("------------------------------Arrange-----------------------------------------------");
get_arrange=np.arange(0,10,2);
print(get_arrange);
print("------------------------------Random-----------------------------------------------");
get_random=np.random.rand(2,5);
print(get_random);
print("------------------------------Zeros-----------------------------------------------");
get_zeros=np.zeros((2,3),order="F");
print(get_zeros);
print("------------------------------Empty-----------------------------------------------");
get_empty=np.empty((2,3),order="C");
print(get_empty);
print("------------------------------Add ten in array-----------------------------------------------");
add_ten=10+get_zeros;
print(add_ten);
print("------------------------------Reshape with arrange-------------------------------------");
get_ten_to_twenty=np.arange(10,20,1);
print(get_ten_to_twenty);
array_reshape=get_ten_to_twenty.reshape(2,-1);
print(array_reshape);
print("------------------------------Flat-------------------------------------");
c_array=np.array([[10,20,30,40],[100,200,300,400],[101,202,303,404]]);
for idx,item in enumerate(c_array.flat):
    print(idx,":",item);
print("------------------------------Flattern-------------------------------------");
flattern_array=c_array.flatten()
print(flattern_array);