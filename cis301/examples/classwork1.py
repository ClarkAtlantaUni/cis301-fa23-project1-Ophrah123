
class Car:

    def __init__(self):
        self.type = None
        self.make = None
        self.model = None
        self.year = None
        self.fuel = None

    #@abstractmethod
    #methods with no definitions
    #def engine_type(self):
        #pass

    #Function that is called when using print statements in an object
    def __str__(self):
        return f"This is a {self.make} {self.model}"

class SUV(Car):
    def __init__(self):
        pass

if __name__ == '__main__':
     c1 = Car()
     c1.make = "BNW"
     c1.model = "320i"
     print("c1", c1)