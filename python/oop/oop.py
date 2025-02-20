class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def display_info(self):
        print(f"Car: {self.brand} {self.model} ({self.year})")
        
    def start_engine(self):
        print("Engine started")
        
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"  # Example of __str__ method
        
# new = Car("Toyota", "Camry", 2022)
# new.display_info()
# new.start_engine()
# print(new)

class Toyota(Car):
    def __init__(self, model, year,owner):
        super().__init__("Toyota", model, year)
        self.__owner = owner
        
    def start_engine(self):
        print(f"Engine {self.brand} started")
        
    def get_owner(self):
        print(self.__owner)

# new = Toyota("Camry", 2024, "John Doe")
# new.display_info()
# new.start_engine()
# print(new)
# print(new.model)
# # print(new.__owner) ## error because its private
# print(new.get_owner())

# call object using function
def toyota_run_all(obj : Toyota):
    engine_sound = obj.start_engine()
    info = obj.display_info()
    owner = obj.get_owner()

    return engine_sound, info, owner

data = [
    {
        "model":"Celica",
        "year":2024,
        "owner":"John"
    },
        {
        "model":"Supra",
        "year":2024,
        "owner":"Kevin"
    },
        {
        "model":"Supra",
        "year":1999,
        "owner":"Alex"
    },
]

for i in data:
    toyota = Toyota(i["model"], i["year"], i["owner"])
    toyota_run_all(toyota)