from cis301.classes.human import Human


class Student(Human):
    """
        This class is represents a Student
        Attributes:
            name:The student’s name.
            classes: The names of the classes the student is taking. A student may take zero or more classes.
            gpa:The student’s grade point average.
    """
    def __init__(self, name, classes, gpa):
       raise NotImplementedError('not implemented yet')

    def says(self):
        """
            All students say "This class is too much work".
        Returns:
            a String statement that says "This class is too much work".
        """
        raise NotImplementedError('not implemented yet')

    def __str__(self):
        """
        Returns:
            a String that describes this Student.
        """
        raise NotImplementedError('not implemented yet')
    @staticmethod
    def main(args):
        """
            Main program that parses the command line, creates a
            Student, and prints a description of the student to
            standard out by invoking its toString method.
            """
        print(f"Missing command line arguments")
        exit(1)

if __name__=="__main__":
    Student.main()
