class A:
    def show(self):
        print("A");
class B(A):
    def show(self):
        print("B");
        super().show();
class C(A):
    def show(self):
        print("C");
        super().show();
class D(B,C):
    def show(self):
        print("D");
        super().show();
if __name__ == "__main__":
    get_go = D();
    get_go.show();