
# ✅ 1. Class

# A class is a blueprint for creating objects.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
# ✅ 2. Object
# An object is an instance of a class.

my_car = Car("toyota", "corolla")
print(f"Brand:{my_car.brand} | Model:{my_car.model} ")
