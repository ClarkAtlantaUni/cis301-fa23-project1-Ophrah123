from cis301.examples.human import Human

class person(Human):

    def

        college = Student()
        # Why you had to add name, classes, gpa to your intstantiation: in heirarchy is called IS-A
        # Reference the superclass human in __init__ to be able to use it.
        college.name = sys.argv[0]
        if college.name == college.name:
            pass
        else:
            print("Please enter a name with only letters.")
        college.classes = sys.argv[2:-1]
        if college.classes == str(college.classes):
            pass
        else:
            print("Please enter your correct classes.")
        college.gpa = sys.argv[1]
        if college.gpa == float(college.gpa):
            pass
        else:
            print("Please enter a correct GPA.")
        college.says()
        # print(college)