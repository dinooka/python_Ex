# class name should star with a capital letter
class Student:
    def __init__(self,std_id,std_name,std_class):
        self.student_id = std_id
        self.student_name = std_name
        self.student_class = std_class
    
    def std_details(self):
        print("Student id : {}".format(self.student_id))
        print("Student name : {}".format(self.student_name))
        print("Student class : {}".format(self.student_class))

    def average(self,marks, no_of_subjects):
        print("Student Average : {}".format(marks/no_of_subjects))

    no_of_leaves = 8

    def print_leaves(self):
        print("No of leaves = {}".format(self.no_of_leaves))
    
    def shout(cls):
        print("Aiyooo!!!")

student_a = Student(17782,"Ricky","11-G")
student_b = Student(16621,"Anna","2-A")

student_a.std_details()
student_a.average(410,5)
student_a.print_leaves()
student_a.shout()

 