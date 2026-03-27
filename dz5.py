class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    def start(self):
        return f"Engine with {self.horsepower} HP started."
class Wheels:
    def __init__(self, count):
        self.count = count
    def rotate(self):
        return f"{self.count} wheels are rotating."
class Vehicle(Engine, Wheels):
    def __init__(self, horsepower, count, brand):
        super().__init__(horsepower)
        Wheels.__init__(self, count)
        self.brand = brand
    def drive(self):
        engine_status = super().start()
        wheels_status = self.rotate()
        return f"{self.brand} is driving.\n{engine_status}\n{wheels_status}"

car = Vehicle(150, 4, "Toyota")
print(car.drive())
