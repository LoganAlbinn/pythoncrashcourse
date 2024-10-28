class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"{self.name}!")

    def instigate(self):
        print(f"{self.name}: You Stink !!!")

    def attack(self, opponent):



        print(f"{self.name} attacks {opponent.name}")
        print(f"{opponent.name} has {opponent.health}")
        print(f"{self.name} does {self.strength}")
        opponent.health = opponent.health - self.strength


character_1 = Character("Elon", 100, 20)
character_2 = Character("X", 150, 15)


print(character_2.health)
print("attacks!")
character_1.attack(character_2)
print(character_2.health)

# print(character_1.name, character_1.health)
# print(character_2.name, character_2.health)

# character_1.greet()
# character_2.greet()

# character_1.instigate()
# character_2.instigate()
   