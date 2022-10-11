class Stack:
    def __init__(self):
        self.internalArray = []

    def push(self, *items):
        for element in items:
            self.internalArray.append(element)

    def pop(self):
        top = self.internalArray[-1]
        del self.internalArray[-1]
        return top

    def peek(self):
        return self.internalArray[-1]

    def __str__(self):
        return self.internalArray.__str__()


people_list = Stack()

people_list.push("Walter")
people_list.push("Jesse")
people_list.push("Mike")
people_list.push("Saul", "Kim")

print(people_list)

print(f"Latest person is {people_list.peek()}")

people_list.pop()

print(f"Latest person is {people_list.peek()}")

print(people_list)
