import random


class Cat:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self):
        self.weight += 1
        print(self.name + " just ate some food.")

    def meow(self):
        print("mrrpp")

    def check_fat(self):
        print(self.name + " is " + str(self.weight) + " fat.")
        if self.weight >= 5:
            print("oh lawd he comin")
        else:
            print("what a lad.")


# Initialize the cats

cat1 = Cat("Binnie", 4, 4)
cat2 = Cat("Clyde", 1, 2)

# Feet the bois

cat1.eat()
cat1.meow()

cat2.eat()
cat2.meow()

# How fat are they

cat1.check_fat()
cat2.check_fat()
