from student import Student
def main():
    student = Student(Human)
    student.name = input("Please enter your name.")
    student.classes = input("Please enter your classes for the semester seperated by a comma.")
    student.gpa = float(input("Please enter your GPA."))