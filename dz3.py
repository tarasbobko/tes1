class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.happiness = 50

    def play(self):
        self.happiness += 10
        print(f"{self.name} грається і стає щасливішим! Рівень щастя: {self.happiness}")

    def feed(self):
        self.happiness += 5
        print(f"{self.name} поїв. Рівень щастя: {self.happiness}")


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.energy = 100
        self.pet = None

    def adopt_pet(self, pet):
        self.pet = pet
        print(f"{self.name} всиновив {pet.name}, який є {pet.species}.")

    def play_with_pet(self):
        if self.pet:
            print(f"{self.name} грається з {self.pet.name}.")
            self.pet.play()
            self.energy -= 5
        else:
            print(f"{self.name} не має домашнього улюбленця.")

    def feed_pet(self):
        if self.pet:
            print(f"{self.name} годує {self.pet.name}.")
            self.pet.feed()
        else:
            print(f"{self.name} не має кого годувати.")



human = Human("Оксана", 25)
dog = Pet("Барсик", "собака")

human.adopt_pet(dog)
human.play_with_pet()
human.feed_pet()
