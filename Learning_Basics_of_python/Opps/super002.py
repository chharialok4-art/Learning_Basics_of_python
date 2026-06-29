class A:
    def show(self):
        print("A");
class B(A):
    def show(self):
        super().show();
        print("B");
class C(A):
    def show(self):
        super().show();
        print("C");
class D(B,C):
    def show(self):
        super().show();
        print("D");
if __name__ == "__main__":
    get_all = D();
    get_all.show();