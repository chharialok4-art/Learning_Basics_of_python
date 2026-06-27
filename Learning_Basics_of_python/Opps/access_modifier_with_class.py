class Board_of_Directors:
    def __init__(self,rank,salary,responsibility,name):
        self.Directors_rank = rank;
        self.__Directors_salary = salary;
        self._Directors_responsibility = responsibility;
        self.Directors_name = name;
    def show_directors_details(self):
        print("Name:",self.Directors_name);
        print("Rank:",self.__Directors_salary);
        print("Resposibility:",self._Directors_responsibility);
        print("salary:",self.Directors_rank);
class Board_of_Managers(Board_of_Directors):
    def __init__(self,
                 d_rank,d_salary,d_responsibility,d_name,
                 m_rank,m_salary,m_responsibility,m_name):
        super().__init__(d_rank,d_salary,d_responsibility,d_name)
        self.Managers_rank = m_rank;
        self.__Managers_salary = m_salary;
        self._Managers_responsibility = m_responsibility;
        self.Managers_name = m_name;
    def show_managers_details(self):
        print("Name:",self.Managers_name);
        print("rank:",self.Managers_rank);
        print("Resposibility:",self._Managers_responsibility);
        print("salary:",self.__Managers_salary);
class Employee(Board_of_Managers):
    def __init__(self,d_rank,d_salary,d_responsibility,d_name,
                 m_rank,m_salary,m_responsibility,m_name,
                 e_rank,e_salary,e_responsibility,e_name):
        super().__init__(d_rank,d_salary,d_responsibility,d_name,
                 m_rank,m_salary,m_responsibility,m_name)
        self.Employee_rank = e_rank;
        self.__Employee_salary = e_salary;
        self._Employee_responsibility = e_responsibility;
        self.Employee_name = e_name;
    def show_employee_details(self):
        print("Name:",self.Employee_name);
        print("Rank:",self.__Employee_salary);
        print("Resposibility:",self._Employee_responsibility);
        print("salary:",self.__Employee_salary);
if __name__ == "__main__":
    emp_001 = Employee("Joint Director",120000,"Supply Chain","Darshi Bhadoriya",
                       "Assistant Manager",50000,"Tech lead","Rahul",
                       "Developer",25000,"google map","Atulya Srivastava");
    print("---------------employee access Director-----------------");
    print(emp_001.show_directors_details());
    print("-----------------emloyee access manager-------------------");
    print(emp_001.show_managers_details());
    print("-----------------emloyee access employee-------------------");
    print(emp_001.show_employee_details());


    
    



    
