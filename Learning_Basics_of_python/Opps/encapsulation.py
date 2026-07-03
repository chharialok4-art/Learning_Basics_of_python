class StateBankOfIndia:
    def __init__(self):
        self.__account_balance = 1000000;
    def deposite(self,credit):
        self.__account_balance += credit;
        print("Net Balance after credit:",self.__account_balance);
    def withdrawl(self,debit):
        if debit <= self.__account_balance:
            self.__account_balance -= debit;
            print("Net Balance after debit:",self.__account_balance);
        else:
            print("-----------------Insuficient Balance------------------");
            print("Total Balance:",self.__account_balance);
    def show_Balance(self):
        print("Total Balance:",self.__account_balance);
if __name__ == "__main__":
    alok_account = StateBankOfIndia();
    print("---------------------DEPOSITE--------------------");
    alok_account.deposite(4000);
    print("---------------------WITHDRAWL--------------------");
    alok_account.withdrawl(1);
    print("-----------------SHOW BALANCE------------------------");
    alok_account.show_Balance();
    alok_account.__account_balance = -4000;
    print(alok_account.__account_balance);
