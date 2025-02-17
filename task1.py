class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")
        print(f"Year: {self.year}")

car1 = Car("Ferari", "F40", 1987)
car2 = Car("BMW", "M4", 2025)

car1.display_info()
print()
car2.display_info()