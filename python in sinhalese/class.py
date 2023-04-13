class Student:
    
    grade = 6
    def walk(self):
        # print(type(self))
        print("This is walk method")
    def greet(self):
        print("Hi Hello!")
           
    @staticmethod
    def marks():
        print("marks method...")

sam = Student()
sam.grade = 7

print(sam.grade)
sam.walk()

ann = Student()
print(ann.grade)
ann.walk()

Student.greet(ann)

Student.marks()