class Student:

  def __init__(self, name,roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  sorted_students=sorted(student_list,key=lambda student: student.cgpa,reverse=True)
  return sorted_students
students = [
    Student("Sujitha", "c23", 6.5),
    Student("Sowmiya", "c24", 7.9),
    Student("Sankar", "c25", 8.9),
    Student("Sangeetha","c26", 9.0),
]

sorted_students =sort_students(students)
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,student.roll_number,student.cgpa))
