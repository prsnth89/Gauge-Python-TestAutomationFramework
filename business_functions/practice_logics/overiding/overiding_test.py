class Animal:
    def bark(self):
        print("animal barks")

class Dog(Animal):
    def bark(self):
        print("dog barks")

class Puppy(Dog):
    def bark(self):
        print("puppy barks")

class Test:
    dog=Dog()
    dog.bark() #dog barks
    
    puppy=Puppy()
    puppy.bark() #puppy barks

