class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"

d = Device("Samsung", "Galaxy Tab")
print(d.info())


class Animal:
    def move(self):
        return "Moving"

class Dog(Animal):
    def move(self):
        return "Running"

class Bird(Animal):
    def move(self):
        return "Flying"

class Fish(Animal):
    def move(self):
        return "Swimming"

animals = [Dog(), Bird(), Fish()]
for a in animals:
    print(a.move())