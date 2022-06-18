class Student:
    def __init__(self, name, course, gpa):
        self.name = name
        self.course = course
        self.gpa = gpa

student1 = Student('James', 'Comp Science', 3.7)
student2 = Student('Angie', 'Bcom', 4.0)

print(student1.course)
print(student2.name)