from cis301.examples.human import Human

class Student(Human):
    """
        This class is represents a Student
        Attributes:
            name:The student’s name.
            classes: The names of the classes the student is taking. A student may take zero or more classes.
            gpa:The student’s grade point average.
    """
    def __init__(self,name,gpa,classes):
        super().__init__(name)
        self.gpa = gpa
        self.classes = classes
        #Better way to uniform things instead of using none

    def says(self):
        """
            All students say "This class is too much work".
        Returns:
            a String statement that says "This class is too much work".
        """
        return "This class is too much work."

    def __str__(self):
        """
        Returns:
            a String that describes this Student.
        """
        return (f"{self.name} has a GPA of {self.gpa} and is taking (len{self.classes}) classes:{self.classes}. "
                f"{self.name} says {self.says}")





