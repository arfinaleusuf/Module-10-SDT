from school import School
from person import Student, Teacher
from subject import Subject
from classroom import ClassRoom


school = School("ABC", "Dhaka")

#  adding classroom
eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

#  Adding student

rohim = Student("rohim", eight)
korim = Student("Korim", nine)
fahim = Student("Fahim", ten)
hamim = Student("Hamim", ten)

school.student_addmission(rohim)
school.student_addmission(korim)
school.student_addmission(fahim)
school.student_addmission(hamim)


# Adding teacher

abul = Teacher("Abul Khan")
babul = Teacher("Babul Khan")
kabul = Teacher("Kabul Khan")

# adding Subject
bangla = Subject("Bangla", abul)
physics = Subject("Physics", babul)
chemistry = Subject("Chemistry", kabul)
biology = Subject("Biology", kabul)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)
nine.add_subject(biology)
nine.add_subject(physics)
nine.add_subject(chemistry)
ten.add_subject(chemistry)
ten.add_subject(bangla)
ten.add_subject(physics)
ten.add_subject(biology)

eight.take_semestar_final_exam() # calling exam
nine.take_semestar_final_exam()
ten.take_semestar_final_exam()

print(school)