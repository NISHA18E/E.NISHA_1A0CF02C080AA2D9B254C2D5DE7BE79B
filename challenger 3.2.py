class Student:
  def __init__(self,name,roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa
    
def sort_students(student_list):
  sorted_students = sorted(student_list,key=lambda student:student.cgpa,reverse=True)
  return sorted_students
  
students = [Student("hari","A123",7.6),Student("Srikanth","A124",8.9),Student("Saumya","A125",9.1),Student("Mahidhar","A126",9.9),]

sort_students = sort_students(students)

for student in sort_students:
  print("Name: {}, Roll Number: {}, cgpa: {}".format(student.name,student.roll_number,student.cgpa))