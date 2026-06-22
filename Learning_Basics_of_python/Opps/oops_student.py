details ={};
class Student:
    no_of_student = 0
    def __init__(self,name,roll_number,standard,course):
        self.student_name = name;
        self.student_roll_number = roll_number;
        self.student_standard = standard;
        self.student_course = course;
        Student.no_of_student = Student.no_of_student + 1
    def student_details_display(self):
        print(f"Name:{self.student_name}");
        print(f"Roll Number:{self.student_roll_number}")
        print(f"Class:{self.student_standard} th")
        print(f"Course:{self.student_course}")
    def no_of_students_college(self):
        print("Total number of Students:",Student.no_of_student);
if __name__ == "__main__":
    alok_chhari = Student("Alok Chhari",100,11,"PCM");
    Amit_chhari = Student("Amit Chhari",200,12,"Political Science");
    Annu_mansingh = Student("Annu Mansingh",300,10,"Social Science");
    Darshi_Singh = Student("Darshi Singh",400,9,"Home Science");
    Chanu_Mansingh = Student("Kabir Singh",500,9,"History");
    alok_chhari.student_details_display();
    print("----------------------------------------------------------------------------")
    Chanu_Mansingh.student_details_display();
    print("----------------------------------------------------------------------------")
    Darshi_Singh.student_details_display();
    print("----------------------------------------------------------------------------")
    Annu_mansingh.student_details_display();
    print("----------------------------------------------------------------------------")
    Amit_chhari.student_details_display();
    print("----------------------------------------------------------------------------")
    Student.no_of_students_college(None);
    details = alok_chhari.__dict__;
    print(details);
    print("--------------------------------------------------------------------------")
    print(Student.__dict__);
