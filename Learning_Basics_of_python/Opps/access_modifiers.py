class AccessModifiers:
    def __init__(self,access_public,access_protected,access_private):
        self.access_public = access_public;
        self._access_protected = access_protected;
        self.__access_private = access_private;
    def show_all(self):
        print(self.access_public);
        print(self._access_protected);
        print(self.__access_private);
if __name__ == "__main__":
    access001 = AccessModifiers("Alok Chhari","Amit Mansingh","Annu Mansingh");
    print("Access001->",access001.show_all());
    print("-------------------------------------------------------------------------------")
    access001.access_public = "Darshi Mansingh";
    access001._access_protected = "Kirti Chhari";
    access001.__access_private = "Divya Mansingh";
    print("Access New->",access001.show_all());