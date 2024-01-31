# simplest form

class MyClass:
    x = 4

p1 = MyClass()
print(p1.x)

# __init__ and __str__

class Person:
    # Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # The __str__() function controls what should be returned when the class object is represented as a string.
    # If the __str__() function is not set, the string representation of the object is returned:
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
    def helloMethod(self):
        print("Hello "+self.name)
    
p1 = Person("John", 36)
print(p1)
p1.helloMethod()


# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
class Person2:
  def __init__(randomSelfName, name, age):
    randomSelfName.name = name
    randomSelfName.age = age

  def myfunc(moreRandomSelfName):
    print("Hello my name is " + moreRandomSelfName.name)

p1 = Person2("John", 36)
p1.myfunc() 

