class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.students = []  # list of studnet object
        self.subjects = []  # list of subject object
    def add_student(self, student):  #rahim, eight e vhorti honbe.
        roll_no = f"{self.name} - {len(self.students) + 1}"
        student.id = roll_no
        self.students.append(student)
        
    def add_subject(self, subject):
        self.subjects.append(subject)

    def take_semestar_final_exam(self):
        for subject in self.subjects:
            subject.evalute_exam(self.students)
        for student in self.students:
            student.calculate_final_grade()