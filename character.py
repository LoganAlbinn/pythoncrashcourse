import random

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

    def damage(self):
        return self.strength + random.randrange(0,int(self.strength/2) - self

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
   

class LCG:
    def __init__(self, seed):
        self.seed = seed
        self.modulus = 2**31 - 1
        self.multiplier = 48271
        self.increment = 0

    def random(self):
        self.seed = self.seed * self.multiplier
        self.seed = self.seed + self.increment
        self.seed = self.seed% self.modulus
        return self.seed
    
lcg = LCG(314159265358979323846264338327950288419716939937510982)
    
for i in range(10):
    print(lcg.random())

