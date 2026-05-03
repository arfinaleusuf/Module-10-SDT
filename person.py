import random
from school import School
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
    def evalute_exam(self):
        return random.randint(1, 100)

class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.Classroom = classroom
        self.__id = None
        self.marks = {}  #{"eng" : 78, "ICT" : 90}
        self.subject_grade = {} # {"english" : "A"}
        self.grade = None
    
    def final_grade(self):
        sum = 0
        for grade in self.subject_grade.values():
            point = School.grade_to_value(grade)
            sum += point
        gpa = sum / len(self.subject_grade)
        self.grade = School.value_to_grade(gpa)

    # rohim .id ==
    @property
    def id(self):
        return self.__id
    
    # rohim.id = 12
    @id.setter
    def id(self, value):
        self.__id == value