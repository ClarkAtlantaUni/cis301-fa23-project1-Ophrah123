import sys
from student import Student
from __init__ import main

def main(args=None):
    """
        This program that parses the command line, creates a
        Student, and prints a description of the student to
        standard out by invoking its toString method.
    """
    if args is None:
        args = sys.argv[1:]

    print (args)
    print(f"Missing command line arguments")
    exit(0)    

def parse_cli_argv(argv):
    raise NotImplementedError('not implemented yet')
    
if __name__ == "__main__":
    college = Student()
    college.name = input("Please enter your name.")
    college.classes = input("Please enter your classes for the semester seperated by a comma.")
    college.gpa = float(input("Please enter your GPA."))
    college.says()
    print(college)

    main()