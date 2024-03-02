class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement the speak method")


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
    
class Lion(Animal):
    def speak(self):
        return f"{self.name} says Grrrrrr!"

# Creating instances of subclasses
dog = Dog("Dog")
cat = Cat("Cat")
lion= Lion("Lion")

# Calling the speak method of each subclass
print(dog.speak())  # Output: Dog says Woof!
print(cat.speak())  # Output: Cat says Meow!
print(lion.speak())  # Output: Lion says Grrrrrr!

