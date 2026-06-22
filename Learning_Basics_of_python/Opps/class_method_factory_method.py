class Cloths:
    price = 4000;
    def set_price(cls,new_price):
        cls.price = new_price;
    def show_price(self):
        return self.price;
if __name__ == "__main__":
    t_shirt = Cloths();
    go_with_price = int(input("enter the price:"));
    t_shirt.set_price(go_with_price);
    print(t_shirt.show_price());
