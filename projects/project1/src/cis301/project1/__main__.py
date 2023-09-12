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
    college.name = sys.argv[0]
    if college.name ==college.name:
        pass
    else:
        print("Please enter a name with only letters.")
    college.classes = sys.argv[3:-1]
    if college.classes ==str(college.classes):
        pass
    else:
        print("Please enter your correct classes.")
    college.gpa = sys.argv[1]
    if college.gpa ==float(college.gpa):
        pass
    else:
        print("Please enter a correct GPA.")
    college.says()
    #print(college)

    main()