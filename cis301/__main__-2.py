import sys

from cis301.project1.student import Student


#from student import Student

def main(args=None):
    """
        This program that parses the command line, creates a
        Student, and prints a description of the student to
        standard out by invoking its toString method.
    """
    print("This is the argv:", sys.argv)
    if args is None:
        args = sys.argv[1:]

    print (args)
    #print(f"Missing command line arguments")
    parse_cli_argv(args)
    #Read in all text from the string and ensure all values are correct
    exit(0)


def isvalidGPA(gpa):
    try:
        if float(gpa):
            return True
        else:
            return False
    except:
        return False


def parse_cli_argv(argv, gpa=None, classes=None):
    if len(argv) < 2:
        print("Please enter the correct information: Name, GPA & Classes.")
        return
    #name of student
    name = argv[0]
    if name == argv[0]:
        pass
    else:
        print("Please enter a name.")
    #gpa
    gpa = argv[1]
    if not isvalidGPA(gpa):
        print("Please enter a valid number for:GPA ")
        return
    #classes
    classes = argv[2:]
    #create a new student instance
    student=Student(name, gpa, classes)
    #print student description
    print(student)


    #raise NotImplementedError('not implemented yet')
    
if __name__ == "__main__":
    main(["ali", 4.0, "301", "431", "475"])
    #main()