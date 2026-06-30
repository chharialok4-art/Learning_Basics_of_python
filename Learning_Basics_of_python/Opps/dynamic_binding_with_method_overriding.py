class Animal:
    def sound(self):
        print("Animal Makes Sound");
class Dog(Animal):
    def sound(self):
        print("Bark Bark");
class Cat(Animal):
    def sound(self):
        print("Meawo Meawo");
def make_sound(ani):
    ani.sound();
if __name__ == "__main__":
    dog = Dog();
    make_sound(dog);
    cat = Cat();
    make_sound(cat);
