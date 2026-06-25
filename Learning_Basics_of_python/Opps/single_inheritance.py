class Vehicle:
    milage = 0;
    def __init__(self,wheel_size,wheel_base,displacement,piston,tank_size,name,range_of_car):
        self.wheel_size = wheel_size;
        self.wheel_base = wheel_base;
        self.displacement = displacement;
        self.piston = piston;
        self.tank_size = tank_size;
        self.name = name;
        self.range_of_car = range_of_car;
    def opertion(self):
        Vehicle.milage = self.range_of_car/self.tank_size;
        return Vehicle.milage;
class Car(Vehicle):
    size = 0 ;
    power = 0;
    def vehicle_size(self):
        Car.size = self.wheel_size + self.wheel_size;
        return Car.size;
    def engine_power(self):
        Car.power = self.displacement/self.piston;
        return Car.power;
    def show_name(self):
        return self.name;
if __name__ == "__main__":
    get_name = str(input("enter the name of vehicle:"));
    get_wheel_size = int(input("enter the wheel size:"));
    get_wheel_base = int(input("enter the wheel base:"));
    get_displacement = int(input("enter the CC:"));
    get_tank_size = int(input("enter the tank size:"));
    get_range_of_car = int(input("enter the range of car:"));
    get_number_of_piston = int(input("enter the number of piston:"));
    breeza = Car(get_wheel_size, get_wheel_base,get_displacement,get_number_of_piston,get_tank_size,get_name,get_range_of_car)
    print("Name:",breeza.show_name());
    print("Milage:",breeza.opertion());
    print("Car Size:",breeza.vehicle_size());
    print("Engine Size:",breeza.engine_power());
    
