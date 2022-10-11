import random


class Cat:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self, amount=1):
        self.weight += amount
        print(f"{self.name} just ate {amount} food.")
        print(f"{self.name}'s weight is now {self.weight}.")

    def diet(self, amount=1):
        if amount >= self.weight:
            print(f"That is too much diet for {self.name}'s weight!")
        else:
            initial_weight = self.weight
            self.weight -= amount
            print(f"{self.name} went on a diet! Their weight went from {initial_weight} to {self.weight}. ")


# Initialize the cats

cat1 = Cat("Binnie", 4, 4)
cat2 = Cat("Clyde", 1, 2)
cat3 = Cat("Old Tom", 10, 6)
# Feed

cat1.eat()
cat2.eat()
cat3.eat()

# Diet

cat1.diet()
cat2.diet()
cat3.diet()