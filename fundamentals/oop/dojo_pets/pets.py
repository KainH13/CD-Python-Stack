class Pet:
    def __init__(self, name, type, sound, tricks, health, energy):
        self.name = name
        self.type = type
        self.sound = sound
        self.tricks = tricks
        self.health = health
        self.energy = energy


    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print(f"{self.name} says {self.sound}!")
        return self