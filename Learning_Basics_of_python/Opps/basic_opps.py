class Customer:
    def __init__(self,wheel,displacement,milage,name):
        self.wheel_size = wheel;
        self.engine_size = displacement;
        self.kilometers = milage;
        self.vahicle_name = name;
    def output_values(self):
        print(f"Manufacturer:{self.vahicle_name}")
        print(f"Wheel Size:{self.wheel_size} inc");
        print(f"Engine Size:{self.engine_size} cc");
        print(f"Car range:{self.kilometers} km");
if __name__ == "__main__":
    get_tank_capacity = int(input("enter the Tank Capacity:"));
    audi = Customer(18,4000,(12*get_tank_capacity),"AUDI");
    mercedece = Customer(20,2500,(15*get_tank_capacity),"MERCEDESE");
    audi.output_values();
    print("--------------------------------------------------")
    mercedece.output_values();
