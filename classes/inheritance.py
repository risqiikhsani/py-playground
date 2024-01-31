from classes import Person

class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.graduationyear = year

    def print_all(self):
        print(self) # will inherit from parent's __str__
        print("graduated in " + str(self.graduationyear))

    def helloMethod(self): # will overide the parent's method because same name
        print("Hello ", self.name, "class of", self.graduationyear) 

x = Student("Mike", 20, 2019)
print(x)
x.print_all()
x.helloMethod()