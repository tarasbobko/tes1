import random

class Student:
    def __init__(self, name, money=100, knowledge=0, energy=100):
        self.name = name
        self.money = money
        self.knowledge = knowledge
        self.energy = energy
        self.day = 0

    def work(self):
        self.money += 20
        self.energy -= 10
        print(f"{self.name} працює. Гроші: {self.money}, Енергія: {self.energy}")

    def study(self):
        self.knowledge += 5
        self.energy -= 15
        print(f"{self.name} навчається. Знання: {self.knowledge}, Енергія: {self.energy}")

    def rest(self):
        self.energy += 20
        self.money -= 5
        print(f"{self.name} відпочиває. Енергія: {self.energy}, Гроші: {self.money}")

    def live_day(self):
        self.day += 1
        print(f"\nДень {self.day}")
        if self.money <= 0:
            self.work()
        elif self.knowledge < 50:
            self.study()
        elif self.energy < 30:
            self.rest()
        else:
            random.choice([self.work, self.study, self.rest])()

# Симуляція року
student = Student("Іван")
for _ in range(365):
    student.live_day()
